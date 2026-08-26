from pathlib import Path
import pandas as pd

# Automatically locate the CSV file in the script's directory
script_dir = Path(__file__).parent
df = pd.read_csv(script_dir / 'dirty_cafe_sales.csv')

# handel values

cat_cols =['Item', 'Payment Method', 'Location']
df[cat_cols] = df[cat_cols].fillna('Unknown')

num_cols = ['Quantity', 'Price Per Unit', 'Total Spent']
df[num_cols] = df[num_cols].apply(pd.to_numeric)

# Fill missing values using math formula
df['Quantity'] = df['Quantity'].fillna(df['Total Spent'] / df['Price Per Unit'])
df['Price Per Unit'] = df['Price Per Unit'].fillna(df['Total Spent'] / df['Quantity'])
df['Total Spent'] = df['Total Spent'].fillna(df['Quantity'] * df['Price Per Unit'])

print(df.isna().sum())
print("-" * 50) 
print(df.shape)
print("-" * 50) 

