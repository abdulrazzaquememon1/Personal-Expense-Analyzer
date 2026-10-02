# Personal Expense Analyzer

A Python-based data analysis project that analyzes personal expense data stored in a CSV file. The project uses Pandas to process the data and Matplotlib to create visualizations.

## Features

- Read expense data from a CSV file
- Display all expense records
- Calculate total expenses
- Calculate average expense
- Find the highest expense
- Find the lowest expense
- Find the highest spending category
- Calculate total spending by category
- Display expenses using a bar chart
- Display expense distribution using a pie chart

## Technologies Used

- Python
- Pandas
- Matplotlib
- CSV

## Project Structure

Personal-Expense-Analyzer/

├── expense_analyzer.py
├── expenses.csv
└── README.md

## Requirements

Python 3.x

Install the required libraries:

pip install pandas matplotlib

## How to Run

Open the project folder in VS Code and open the terminal.

Run:

python expense_analyzer.py

## Dataset

The project uses a CSV file named:

expenses.csv

The dataset contains the following information:

- Date
- Category
- Description
- Amount

Example:

Date,Category,Description,Amount

2026-09-01,Food,Lunch,350

2026-09-02,Transport,Bus,150

2026-09-03,Shopping,Shirt,2500

## Analysis Performed

### Total Expense

Calculates the total amount spent across all recorded expenses.

### Average Expense

Calculates the average amount spent per transaction.

### Highest Expense

Finds the transaction with the highest amount.

### Lowest Expense

Finds the transaction with the lowest amount.

### Expense by Category

Groups expenses by category and calculates the total amount spent in each category.

### Highest Spending Category

Identifies the category with the highest total spending.

## Data Visualization

The project uses Matplotlib to visualize the expense data.

### Bar Chart

The bar chart compares the total spending across different categories.

### Pie Chart

The pie chart shows the percentage distribution of spending across categories.

## What I Learned

This project helped me practice:

- Python
- Pandas
- Reading CSV files
- DataFrames
- Grouping data
- Data aggregation
- Calculating statistics
- Data visualization
- Matplotlib

## Future Improvements

Possible improvements include:

- Add monthly expense analysis
- Add date-based filtering
- Add budget tracking
- Add income and savings analysis
- Add more visualizations
- Add a graphical user interface
- Export analysis reports

## Conclusion

The Personal Expense Analyzer demonstrates how Python can be used to process, analyze, and visualize real-world tabular data.

The project provided practical experience with Pandas, CSV data, data aggregation, and visualization using Matplotlib.
