from turtle import reset

import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

raw_data = {
    'Order_ID': ['ORD_501', 'ORD_502', 'ORD_503', 'ORD_504', 'ORD_505', 'ORD_506', 'ORD_507', 'ORD_508', 'ORD_509', 'ORD_510', 'ORD_508', 'ORD_502'],
    'Category': ['Electronics', '  clothing ', 'ELECTRONICS', 'Home', 'Electronics', 'Clothing', 'home & kitchen', 'Electronics', 'UNKNOWN', 'Home', 'Electronics', '  clothing '],
    'Item_Price': ['$1,200.00', '$45.50', '$150.00', 'ERROR', '$800.00', '$25.00', '$60.00', '$1,200.00', '$30.00', '$150.00', '$1,200.00', '$45.50'],
    'Quantity': [1, 2, -1, 3, 0, 4, 1, 1, 2, 500, 1, 2],
    'Total_Amount': [1200.00, 91.00, -150.00, np.nan, 0.00, 100.00, 60.00, 1200.00, 60.00, 75000.00, 1200.00, 91.00],
    'Discount_Pct': ['10%', '0%', '5%', '15%', '0%', '500%', '10%', '10%', '0%', '0%', '10%', '0%'],
    'Order_Date': ['2024-03-01', '03/02/2024', '2024-03-03', '2024-03-04', '2024-03-05', '2024-03-06', '2024-03-07', '2024-03-01', '2024-03-08', '2024-03-09', '2024-03-01', '03/02/2024']
}

df = pd.DataFrame(raw_data)

# remova duplicate value from primary key 
df.drop_duplicates(subset=['Order_ID'],inplace=True)


#Category
df['Category'] = df['Category'].str.title().str.strip()

# Item_Price
df['Item_Price'] = df['Item_Price'].str.replace('$',' ',regex=False)
df['Item_Price'] = df['Item_Price'].str.replace(',', '', regex=False)
df['Item_Price'] = pd.to_numeric(df['Item_Price'], errors='coerce')

# handel nan value
df['Item_Price'] = df['Item_Price'].fillna(df['Item_Price'].mean()).round(2)


#Quantity 
Quantity_datatype=df['Quantity'] = pd.to_numeric(df['Quantity'],errors='coerce')
df['Quantity'] = df['Quantity'].abs()


# Total_Amount
np.set_printoptions(suppress=True)
df['Total_Amount'] = df['Total_Amount'].abs()
# handel nan value 
df['Total_Amount'] = df['Total_Amount'].fillna(df['Item_Price'] * df['Quantity'])


#Discount_Pct

df['Discount_Pct'] = df['Discount_Pct'].str.replace('%',' ',regex=False)
df['Discount_Pct'] = pd.to_numeric(df['Discount_Pct'], errors='coerce')
df.loc[df['Discount_Pct'] > 100, 'Discount_Pct'] = np.nan
df['Discount_Pct'] = df['Discount_Pct'].fillna(0)



#Order_Date
df['Order_Date'] = pd.to_datetime(df['Order_Date'],errors='coerce')
df['Order_Date'] = df['Order_Date'].dt.strftime('%d-%m-%y')
df['Order_Date'] = df['Order_Date'].ffill()

unique_val=df['Discount_Pct'].unique()
print(unique_val,'\n')

print(df)