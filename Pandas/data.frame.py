import pandas as pd

data = [
    {"order_id": 1001, "customer": "Fenil", "category": "Electronics", "amount": 250, "status": "Completed"},
    {"order_id": 1002, "customer": "Ankit", "category": "Furniture", "amount": 450, "status": "Completed"},
    {"order_id": 1003, "customer": "Rahul", "category": "Electronics", "amount": 120, "status": "Cancelled"},
    {"order_id": 1004, "customer": "Priya", "category": "Stationery", "amount": 35, "status": "Completed"},
    {"order_id": 1005, "customer": "Karan", "category": "Electronics", "amount": 800, "status": "Completed"},
    {"order_id": 1006, "customer": "Sonia", "category": "Furniture", "amount": 150, "status": "Pending"}
]

# 1. Create DataFrame first
df = pd.DataFrame(data)

# 2. Rename columns on the DataFrame
df.rename(columns={'customer': 'user', 'order_id': 'id'}, inplace=True)



# print(df.head(2))
# print('----------------------------------------------------')
# print(df.tail(2))
# print(df.shape)
# print(df.columns)

# print(df)
# print(df.describe())

df.to_csv('test.csv',index=False)
df1=pd.read_csv('test.csv')

print(df1)