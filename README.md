# Greenhouse Gas Emissions Analysis

This project analyzes and visualizes greenhouse gas emissions data across different countries from 1990 to 2020. It provides various data visualization tools to understand emission patterns and trends.

## Features

- Data cleaning and preprocessing
- Total emissions calculation
- Top emission countries analysis
- Multiple visualization types:
  - Pie charts for emission distribution
  - Line charts for temporal trends
  - Bar charts for comparative analysis

## Requirements

- Python 3.x
- pandas
- matplotlib

## Installation

1. Clone this repository:
```bash
git clone [your-repository-url]
```

2. Install required packages:
```bash
pip install pandas matplotlib
```

## Usage

The main script `Assignment1.py` contains several functions for data analysis and visualization:

### Data Processing Functions
- `read_csv(file_path)`: Reads the CSV data file
- `clean_data(source_data, data_cols, drop_col)`: Cleans and preprocesses the data
- `total_emission_data(source_data, columns)`: Calculates total emissions
- `top_emission_data(dataframe, col, rows)`: Identifies top emitting countries

### Visualization Functions
- `pie_chart(plot_data, data_point_col, item_col, title)`: Creates pie charts
- `line_chart(plot_data, x_label, y_label, title)`: Creates line charts
- `bar_chart(dataframe, item, data_col, x_label, y_label, title)`: Creates bar charts

## Data

The project uses greenhouse gas emissions data from 1990 to 2020, including:
- Country-wise emissions
- Year-wise trends
- Total emissions calculations

## Output

The script generates three types of visualizations:
1. Pie chart showing the distribution of emissions among top emitting countries
2. Line chart displaying emission trends from 1990 to 2020
3. Bar chart comparing emissions of top countries in the year 2000

## Contributing

Feel free to submit issues and enhancement requests!

## License

[Your chosen license]

## Author

Created by Vijay M
