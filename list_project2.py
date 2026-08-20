from functools import total_ordering


inventory = [
    [101, "Wireless Mouse", "Electronics", 45, 20],
    [102, "Mechanical Keyboard", "Electronics", 8, 80],
    [103, "Office Chair", "Furniture", 15, 150],
    [104, "USB-C Cable", "Electronics", 120, 10],
    [105, "Standing Desk", "Furniture", 4, 450],
    [106, "Notebook", "Stationery", 200, 3]
]

# add new product 
inventory.append([107, "Monitor Stand", "Furniture", 25, 40])  
# print(inventory)


# Calculate Total Inventory Value

Total_Inventory_Value = []
for item_value in inventory :
    Total_Inventory_Value.append(item_value[4])

# print(Total_Inventory_Value)


# Identify Low Stock Items
low_stock_item= []
for item in inventory :
    name = item[2]
    stock = item[3]
    if stock <= 10 :
        low_stock_item.append(f'{name},{stock}')

# for low_stock in low_stock_item:
#     print(low_stock)
    
# Electronics Category Breakdown
Electronics_Category = []
for item in inventory:
    if item[2] == 'Electronics':
        Electronics_Category.append(item[1])

for item in Electronics_Category:
    print(item)