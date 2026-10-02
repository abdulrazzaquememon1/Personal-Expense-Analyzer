import pandas as pd
import matplotlib.pyplot as plt


# Read the expense data
df = pd.read_csv("expenses.csv")


# Display all expenses
print("\n========== ALL EXPENSES ==========")
print(df)


# Calculate total expense
total_expense = df["Amount"].sum()
print("\nTotal Expense:", total_expense)


# Calculate average expense
average_expense = df["Amount"].mean()
print("Average Expense:", round(average_expense, 2))


# Find highest expense
highest_expense = df["Amount"].max()
print("Highest Expense:", highest_expense)


# Find lowest expense
lowest_expense = df["Amount"].min()
print("Lowest Expense:", lowest_expense)


# Find details of the highest expense
highest_record = df.loc[df["Amount"].idxmax()]

print("\n========== HIGHEST EXPENSE ==========")
print("Date:", highest_record["Date"])
print("Category:", highest_record["Category"])
print("Description:", highest_record["Description"])
print("Amount:", highest_record["Amount"])


# Calculate total expense for each category
category_expenses = df.groupby("Category")["Amount"].sum()

print("\n========== EXPENSE BY CATEGORY ==========")
print(category_expenses)


# Find category with highest spending
highest_category = category_expenses.idxmax()
highest_category_amount = category_expenses.max()

print("\nHighest Spending Category:", highest_category)
print("Amount Spent:", highest_category_amount)


# Create bar chart
plt.figure(figsize=(8, 5))

category_expenses.plot(kind="bar")

plt.title("Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount")

plt.tight_layout()
plt.show()


# Create pie chart
plt.figure(figsize=(7, 7))

category_expenses.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Expense Distribution")
plt.ylabel("")

plt.tight_layout()
plt.show()