# 1. Import the Pandas library and give it the standard nickname 'pd'
from unicodedata import category

import pandas as pd

# 2. Raw data stored as a list of dictionaries 
data = [
    {"order_id": 1001, "customer": "Fenil", "category": "Electronics", "amount": 250, "status": "Completed"},
    {"order_id": 1002, "customer": "Ankit", "category": "Furniture", "amount": 450, "status": "Completed"},
    {"order_id": 1003, "customer": "Rahul", "category": "Electronics", "amount": 120, "status": "Cancelled"},
    {"order_id": 1004, "customer": "Priya", "category": "Stationery", "amount": 35, "status": "Completed"},
    {"order_id": 1005, "customer": "Karan", "category": "Electronics", "amount": 800, "status": "Completed"},
    {"order_id": 1006, "customer": "Sonia", "category": "Furniture", "amount": 150, "status": "Pending"}
]

# 3. Convert the raw list into a Pandas DataFrame (creates a table grid with rows and columns)
df = pd.DataFrame(data)
# df.head(3)

# --- PRINTING OPTIONS ---

# -> Displays the complete table grid with row index numbers on the left
# print(df)

# -> Shows column data types (int, string), total row count, and missing values check
# print(df.info())

# -> Calculates instant math stats (mean, min, max, std dev) for all numerical columns
# print(df.describe())

# 1. Total Metrics
total_profit = df['amount'].sum()
total_orders = len(df)

# 2. Filter once and reuse
pending_df = df[df['status'] == 'Pending']['category'].values[0]
pending_count = len(df[df['status'] == 'Pending'])
pending_amount = df[df["status"] == 'Pending']['amount'].sum()

completed_df = df[df['status'] == 'Completed']
completed_count = len(completed_df)
completed_profit = completed_df['amount'].sum()

 #Top customers
top_customer = df.loc[df['amount'].idxmax(), ['customer', 'amount']]

# Group by category and sum up the amount
category_sales = df.groupby('category')['amount'].sum()

print(f"Total Profit: {total_profit} | Total Orders: {total_orders}")
print(f"Completed Orders: {completed_count} | completed order profit: {completed_profit}")
print(f'Pending Orders: {pending_count} | Pending category: {pending_df} | Pending amount: {pending_amount}')
print('top customer')
print(top_customer)
print("\n--- Sales by Category ---")
print(category_sales)



