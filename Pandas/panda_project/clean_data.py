# import numpy as np
import pandas as pd

# 1. Create raw messy dataset
raw_data = {
    "emp_id": [101, 102, 103, 104, 105, 102, 106, 107],  # Includes duplicate (102)
    "full_name": [
        "  fenil PATEL ",
        "ANKIT SHARMA",
        "rahul verma",
        "Priya ",
        "Karan",
        "ANKIT SHARMA",
        "sonia mehta",
        "",
    ],  # Trailing spaces, mixed case, empty spaces
    "department": [
        "IT",
        "HR",
        "it",
        "Finance",
        "N/A",
        "HR",
        "finance",
        "IT",
    ],  # Inconsistent casing & 'N/A' placeholder
    "salary": [
        "$85,000",
        "62000",
        "75,000.00",
        "unknown",
        "110000",
        "62000",
        "-5000",
        "90000",
    ],  # Strings, currency symbols, invalid text, negative number
    "join_date": [
        "2022/01/15",
        "20-06-2021",
        "Jan 12, 2023",
        "2020-11-01",
        "2019.08.05",
        "20-06-2021",
        "invalid_date",
        None,
    ],  # Mixed date formats & corrupt values
}

df = pd.DataFrame(raw_data)

# Fix casing for names and departments
df['full_name'] = df['full_name'].str.title()
df['department'] = df['department'].str.upper()

# replace text N/A to unknown 
df['department'] = df['department'].replace('N/A' , 'unknown')

# 3. Remove duplicate rows based on emp_id
df=df.drop_duplicates(subset=['emp_id'])

# change data type according to data salary & join_date
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df['join_date'] = pd.to_datetime(df['join_date'],format='mixed' ,errors='coerce')

# add month column
df['month'] = df['join_date'].dt.strftime('%b')

# remove extar space from colums
df['full_name'] = df['full_name'].str.strip()

# 1. Clean characters: strip whitespace, remove '$' and ','
df['salary'] = (
    df['salary']
    .astype(str)
    .str.strip()
    .str.replace(r'[\$,]', '', regex=True)
)

# 2. Convert to numeric (turns invalid strings like 'unknown' to NaN)
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')

# 3. Make all numbers positive
df['salary'] = df['salary'].abs()

# 4. Fill missing values with median (or keep as NaN / fill with 0 based on preference)
df['salary'] = df['salary'].fillna(df['salary'].median())

# check null and empty value
# salary        3
# join_date     2
# month         2
# df= df.isna().sum()

# handel null and empty values
df = df.fillna({
    'emp_id': -1,
    'full_name': 'Unknown',
    'department': 'UNKNOWN',
    'salary': 0,
    'join_date': pd.NaT,
    'month': 'Unknown'
})

print(df)
# df.to_csv('cleaned_data.csv',index=False)