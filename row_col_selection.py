import pandas as pd

# Clean sample DataFrame using pure Pandas
data = [
    {"order_id": 1001, "customer": "Fenil", "category": "Electronics", "amount": 250, "status": "Completed"},
    {"order_id": 1002, "customer": "Ankit", "category": "Furniture", "amount": 450, "status": "Completed"},
    {"order_id": 1003, "customer": "Rahul", "category": "Electronics", "amount": 120, "status": "Cancelled"},
    {"order_id": 1004, "customer": "Priya", "category": "Stationery", "amount": 35, "status": "Completed"},
    {"order_id": 1005, "customer": "Karan", "category": "Electronics", "amount": 800, "status": "Completed"},
    {"order_id": 1006, "customer": "Sonia", "category": "Furniture", "amount": 150, "status": "Pending"}
]
df = pd.DataFrame(data)
# print(df[['order_id','city','customer_name']])
# select_rows = df.loc[(df.customer == 'Fenil') & (df.amount >= 300)]
# print(select_rows)

# print(df.iloc[0:3])
# 1. Filter completed orders once
fillter_by_amount = df[df['status'] == 'Completed']

# 2. Derive metrics directly from the filtered DataFrame
total_order = len(fillter_by_amount)
total_profit = fillter_by_amount['amount'].sum()

print(f'total order : {total_order}')
print(f'total profit : ${total_profit}\n\n')

# Hide index numbers for a cleaner table print
print(fillter_by_amount.to_string(index=False))