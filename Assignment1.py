#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 17:23:58 2023

@author: vijaym
"""

import pandas as pd
import matplotlib.pyplot as plt


def read_csv(file_path):
    ''' read_csv is a function with input parameters file_path 
    used to read the file path of given data'''
    return pd.read_csv(file_path)


def clean_data(source_data, data_cols, drop_col):
    '''fuction used to clean the pandas data frame and dropping the column, 
    source_date = Pandas dataframe
    data_cols = column in pandas df
    drop_col = columns to clean'''
    for column in data_cols:
        source_data[column] = source_data[column].astype(float).astype(int)
    clean_data = source_data.drop(columns=drop_col)
    return clean_data


def total_emission_data(source_data, columns):
    ''' function to create new column in the pandas dataframe
    where new column data is the sum of all columns '''

    source_data["total_emissions"] = source_data[columns].sum(axis=1)
    return source_data


def top_emission_data(dataframe, col, rows):
    '''function to sort the data and give first 6 rows of data'''
    dataframe.sort_values(by=col, ascending=False, inplace=True)
    top_df = dataframe.head(rows)
    return top_df


def pie_chart(plot_data, data_point_col, item_col, title):
    '''function to create pie plot with input parameters
    plot_data = pandas dataframe
    data_point_col,item_col = columns in pandas dataframe
      '''
    # Create a line Plot
    plt.figure(figsize=(30.0, 10.0))

    plt.pie(plot_data[data_point_col],
            labels=plot_data[item_col],
            autopct="%0.1f%%", pctdistance=0.9, startangle=40,
            explode=(0.01, 0, 0, 0, 0, 0)
            )
    # Add Title
    plt.title(title)

    # Add legends
    plt.legend(loc="upper right")

    # Show the plot
    plt.show()
    return


def line_chart(plot_data, x_label, y_label, title):
    ''' line_chart is a function with input parameters
    plot_data is the pandas dataframe,x_label,y_label,title are the labels
    used in creating the line chart
            '''
    # Create a line Plot
    plt.figure(figsize=(18.0, 10.0), dpi=440)
    for column in plot_data.columns:
        plt.plot(plot_data.index, plot_data[column], marker='o', label=column)

    # Add Labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Add Legend
    plt.legend(loc="upper left")
    plt.ticklabel_format(style='plain', axis='y')

    # Add Grid lines
    plt.grid(True)

    # Show the plot
    plt.show()
    return


def bar_chart(dataframe, item, data_col, x_label, y_label, title):
    '''function to create bar plot with input parameters
    dataframe = dataframe containing top emissions with 6 rows
    item,data_col are the columns in pandas dataframe 
    x_label,y_label,title are label to create the bar chart'''
    # Create a Bar Plot
    plt.figure(figsize=(9, 6))
    plt.bar(dataframe[item],
            dataframe[data_col],
            width=0.35, align="center")

    # Add Labels and title
    plt.title(title)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=13)

    # Add Grid lines
    plt.grid(True)

    # Rotate x-axis labels for better readibility
    plt.xticks(rotation=45)
    plt.ticklabel_format(style='plain', axis='y')

    # Show the plot
    plt.tight_layout()
    plt.show()
    return


if __name__ == '__main__':

    # reading csv file
    source_data = read_csv('/Users/vijaym/Downloads/Green house data1.csv')

    # Create a array of years
    columns_to_clean = ["1990", "2000", "2013", "2014", "2015", "2016",
                        "2017", "2018", "2019", "2020"]

    # Cleaning data & dropping Column name
    cleansed_data = clean_data(source_data, columns_to_clean, 'Series Name')

    #
    total_emission_df = total_emission_data(cleansed_data, columns_to_clean)

    # Create top emission dataframe with 6 rows
    top_emission_df = top_emission_data(
        total_emission_df, 'total_emissions', 6)

    # Calling pie_chart function
    pie_chart(top_emission_df, 'total_emissions', 'Country Name',
              "Countries with the highest proportions of Greenhouse Gas emissions during 1990 – 2020")

    # Copying the data
    line_plot_data_copy = top_emission_df.copy()

    # Dropping the total emissions column
    line_plot_data = line_plot_data_copy.drop(columns=['total_emissions'])

    # Setting Country name as index
    line_plot_data.set_index('Country Name', inplace=True, drop=True)

    # Create Transpose
    line_plot_data = line_plot_data.transpose()

    # Calling line_chart function
    line_chart(line_plot_data, 'Year', 'Million Metric tons of CO2 Equivalent',
               'Global Greenhouse Emission of Different Countries from 1990-2020')
    # Calling bar_chart function
    bar_chart(top_emission_df, 'Country Name', '2000', 'Countries',
              'Million Metric tons of CO2 Equivalent',
              'Green House Emissions of top 6 countries in the year(2000)')
