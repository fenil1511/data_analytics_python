# from unicodedata import category

orders = [
    {"order_id": 1001, "customer": "Fenil", "category": "Electronics", "amount": 250, "status": "Completed"},
    {"order_id": 1002, "customer": "Ankit", "category": "Furniture", "amount": 450, "status": "Completed"},
    {"order_id": 1003, "customer": "Rahul", "category": "Electronics", "amount": 120, "status": "Cancelled"},
    {"order_id": 1004, "customer": "Priya", "category": "Stationery", "amount": 35, "status": "Completed"},
    {"order_id": 1005, "customer": "Karan", "category": "Electronics", "amount": 800, "status": "Completed"},
    {"order_id": 1006, "customer": "Sonia", "category": "Furniture", "amount": 150, "status": "Pending"}
]


# add new data 
orders.append({"order_id": 1007, "customer": "Meera", "category": "Electronics", "amount": 310, "status": "Completed"})
# for item in orders:
#     print(item)

# revenue of completed orders

completed_orders=[]

for item in orders:
    if item['status'] == 'Completed':
        completed_orders.append(item)

for item in completed_orders:
    print(f'Revenue of completed orders : {item}')

#High-Value Customers
vip_customers = []
for item in orders:
    if item['amount'] >= 300:
        vip_customers.append(item)

for item in vip_customers:
    print(f'High-Value Customers : {item}')


# Electronics Category Spending 

Electronics_Category = []
for item in orders:
    # Check category AND ignore "Cancelled" orders
    if item['category'] == 'Electronics' and item['status'] != 'Cancelled':
      Electronics_Category.append(item['amount'])

total_profit = sum(Electronics_Category)

print(f'Electronics Category Spending : {Electronics_Category}')
print(f'total revenue from the electronics category : {total_profit}')

