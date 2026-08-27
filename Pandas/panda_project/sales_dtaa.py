from statistics import mean, quantiles

import pandas as pd
import numpy as np

# Real-world dirty dataset (50 rows)
raw_data = {
    ' Transaction ID ': [f'TXN_{1000+i}' for i in range(50)],
    'Item_Name': [
        'Coffee', ' Tea ', 'UNKNOWN', 'Cake', 'Sandwich', 'Coffee', 'ERROR', 'Tea', 'Cookie', 'Smoothie',
        ' coffee', 'Tea', 'Juice', 'Cake', np.nan, 'Sandwich', 'Cookie', 'ERROR', 'Smoothie', 'Coffee',
        'Tea', 'UNKNOWN', 'Cake', 'Juice', 'Sandwich', 'Coffee', 'Cookie', 'Tea ', 'ERROR', 'Smoothie',
        'Cake', 'Juice', np.nan, 'Coffee', 'Tea', 'Sandwich', 'UNKNOWN', 'Cookie', 'Smoothie', 'Cake',
        'Coffee', 'Tea', 'Juice', 'Sandwich', 'Cookie', 'ERROR', 'Smoothie', 'Cake', 'Coffee', 'Tea'
    ],
    'Quantity': [
        '2', '1', 'ERROR', '3', '2', '100', '1', '2', '4', 'NaN',
        '3', '1', '2', 'ERROR', '5', '1', 'UNKNOWN', '2', '3', '1',
        '2', '4', '1', '2', 'ERROR', '3', '2', '1', '5', '2',
        'NaN', '2', '1', '3', '2', 'UNKNOWN', '1', '4', '2', '3',
        '1', '2', '3', '1', '2', '5', 'UNKNOWN', '2', '1', '3'
    ],
    'Price_Per_Unit': [
        3.5, 2.0, 4.0, 4.5, 6.0, 3.5, 5.0, np.nan, 2.5, 5.0,
        3.5, 2.0, 'ERROR', 4.5, 6.0, 6.0, 2.5, 5.0, 5.0, 3.5,
        2.0, 2.5, 4.5, 4.0, 'UNKNOWN', 3.5, 2.5, 2.0, 4.5, 5.0,
        4.5, 4.0, 3.5, 3.5, 2.0, 6.0, 4.0, 2.5, 5.0, 4.5,
        3.5, 2.0, 4.0, 6.0, 2.5, 5.0, 5.0, 4.5, 3.5, np.nan
    ],
    'Total_Spent': [
        7.0, 2.0, 8.0, 13.5, 12.0, 350.0, 'UNKNOWN', 4.0, 10.0, 15.0,
        10.5, 2.0, 8.0, 13.5, 30.0, 6.0, 10.0, 10.0, 15.0, 3.5,
        4.0, 10.0, 4.5, 8.0, 12.0, 10.5, 5.0, 2.0, 22.5, 10.0,
        13.5, 8.0, 3.5, 10.5, 4.0, 6.0, 4.0, 10.0, 10.0, 13.5,
        3.5, 4.0, 12.0, 6.0, 5.0, 25.0, 10.0, 9.0, 'ERROR', 6.0
    ],
    'Payment_Method': [
        'Cash', 'Credit Card', np.nan, 'ERROR', 'Digital Wallet', 'UNKNOWN', 'Cash', 'Credit Card', 'Cash', 'Digital Wallet',
        'Credit Card', 'Cash', 'Digital Wallet', 'Cash', 'Credit Card', 'Digital Wallet', np.nan, 'Cash', 'Credit Card', 'Cash',
        'Digital Wallet', 'Cash', 'Credit Card', 'ERROR', 'Digital Wallet', 'Cash', 'Credit Card', 'Cash', 'Digital Wallet', 'UNKNOWN',
        'Cash', 'Digital Wallet', 'Credit Card', 'Cash', 'Digital Wallet', 'Cash', 'Credit Card', np.nan, 'Cash', 'Digital Wallet',
        'Credit Card', 'Cash', 'Digital Wallet', 'Cash', 'Credit Card', 'Digital Wallet', 'Cash', 'Credit Card', 'UNKNOWN', 'Cash'
    ],
    'Date': [
        '2024-01-15', '2024-01-15', '15/01/2024', 'invalid_date', '2024-01-16', '2024-01-16', np.nan, '2024-01-17', '2024-01-17', '2024-01-18',
        '2024-01-18', '2024-01-19', '2024-01-19', '2024/01/20', '2024-01-20', '2024-01-21', '2024-01-21', '2024-01-22', '2024-01-22', '2024-01-23',
        '2024-01-23', '2024-01-24', '2024-01-24', '2024-01-25', '2024-01-25', '2024-01-26', '2024-01-26', '2024-01-27', '2024-01-27', '2024-01-28',
        '2024-01-28', '2024-01-29', '2024-01-29', '2024-01-30', '2024-01-30', '2024-01-31', '2024-01-31', '2024-02-01', '2024-02-01', '2024-02-02',
        '2024-02-02', '2024-02-03', '2024-02-03', '2024-02-04', '2024-02-04', '2024-02-05', '2024-02-05', '2024-02-06', '2024-02-06', '2024-02-07'
    ]
}

df = pd.DataFrame(raw_data)

#change data type
df['Price_Per_Unit'] = pd.to_numeric(df['Price_Per_Unit'], errors='coerce')
df['Total_Spent'] = pd.to_numeric(df['Total_Spent'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'],errors='coerce',format='mixed')
df['Date'] = df['Date'].dt.strftime('%y-%m-%d')



# apply changes on Item_name column 
df['Item_Name'] = df['Item_Name'].astype(str).str.title().str.strip()
df['Item_Name'] = df['Item_Name'].replace(['Error','Unknown'],'Unknown').fillna('Unknown')



# apply changes on Quantity column
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0).astype('Int64')
# Correct reassignment drop
df.drop(df[df['Quantity'] == 100].index, inplace=True)


# changes on Price_Per_Unit 
df['Price_Per_Unit'] = df['Price_Per_Unit'].replace([np.inf, 'inf'], np.nan)
inferred_price = df['Total_Spent'] / df['Quantity'].replace(0, np.nan)
df['Price_Per_Unit'] = df['Price_Per_Unit'].fillna(inferred_price)
df['Price_Per_Unit'] = df['Price_Per_Unit'].fillna(df['Price_Per_Unit'].median())

# apply changes on  Total_Spent
df['Total_Spent'] = df['Total_Spent'].fillna(df['Quantity'] * df['Price_Per_Unit'])



# change in Payment_Method 
df['Payment_Method'] =df['Payment_Method'].str.title()
df['Payment_Method'] = df['Payment_Method'].replace(['Error', 'Unknown'], 'Unknown method').fillna('Unknown method')


# date 
df['Date'] = df['Date'].fillna('No Date')

unique_val= df['Price_Per_Unit'].unique()
print(unique_val)
# print('-'*100,'\n')

print(df)

# df.info()
# print('-'*100,'\n')
print(df.isna().sum())