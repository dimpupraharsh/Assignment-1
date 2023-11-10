#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:02:01 2023

@author: vijaym
"""

import pandas as pd
import matplotlib.pyplot as plt

# Define a fuction to create a bar plot
#def emissions 

# Extracting and sorting the data
data = pd.read_csv("/Users/vijaym/Downloads/Green house data1.csv")

# sorting the data
data1 = data.sort_values(by='2020', ascending=False, inplace=True)
data1 = data.head(10)
colours = ['red','blue','green','orange','yellow','light blue']
# Create a Bar Plot
plt.figure(figsize=(9, 6))
plt.bar(data1["Country Name"], data1["2000"],
        width=0.35, align="center")

# Add Labels and title
plt.title("Greenhouse Gas Emissions of the top 6 countries in recent year (2020) ")
plt.xlabel("Countries", fontsize=12)
plt.ylabel("Million Metric tons of CO2 Equivalent", fontsize=13)

# Add Grid lines
plt.grid(True)

# Rotate x-axis labels for better readibility
plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='y')

# Add legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()

# To save the plot to a file
plt.savefig("Green house emissions.jpeg")

# Call the Fuction to create bar plot
