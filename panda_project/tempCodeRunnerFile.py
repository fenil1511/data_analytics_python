df['full_name'] = df['full_name'].str.title()
# df['department'] = df['department'].str.upper()

# # replace text N/A to unknown 
# df['department'] = df['department'].replace('N/A' , 'unknown')

# # 3. Remove duplicate rows based on emp_id
# df=df.drop_duplicates(subset=['emp_id'])

# # change data type according to data salary & join_date
# df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
# df['join_date'] = pd.to_datetime(df['join_date'],format='mixed' ,errors='coerce')

# # add month column
# df['month'] = df['join_date'].dt.strftime('%b')

# # remove extar space from colums
# df['full_name'] = df['full_name'].str.strip()

# # salry value change neg to pos
# df['salary'] = df['salary'].abs()

# # check null and empty value
# # salary        3
# # join_date     2
# # month         2
# # df= df.isna().sum()

# # handel null and empty values
# df = df.fillna({
#     'emp_id': -1,
#     'full_name': 'Unknown',
#     'department': 'UNKNOWN',
#     'salary': 0,
#     'join_date': pd.NaT,
#     'month': 'Unknown'
# })