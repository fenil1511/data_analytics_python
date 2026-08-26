from os import name

import pandas as pd

# DataFrame 1: Employee details
df_employees = pd.DataFrame([
    {"emp_id": 101, "name": "Fenil", "dept_id": "D1", "salary": 85000},
    {"emp_id": 102, "name": "Ankit", "dept_id": "D2", "salary": 62000},
    {"emp_id": 103, "name": "Rahul", "dept_id": "D1", "salary": 75000},
    {"emp_id": 104, "name": "Priya", "dept_id": "D3", "salary": 90000},
    {"emp_id": 105, "name": "Karan", "dept_id": "D5", "salary": 110000}, # Unmatched dept_id
    {"emp_id": 106, "name": "Sonia", "dept_id": "D6", "salary": 58000}   # Missing dept_id
])

# DataFrame 2: Department details
df_departments = pd.DataFrame([
    {"dept_id": "D1", "dept_name": "IT", "location": "Building A"},
    {"dept_id": "D2", "dept_name": "HR", "location": "Building B"},
    {"dept_id": "D3", "dept_name": "Finance", "location": "Building A"},
    {"dept_id": "D4", "dept_name": "Marketing", "location": "Building C"} # Unmatched department
])
# change data type => emp_id
# df_employees['emp_id'] = pd.to_numeric(df_employees['emp_id']) 
# print(df_employees)

# print("--- Employees ---")
# print(df_employees)

# print("\n--- Department?s ---")
# print(df_departments)


#concat two DF 
# join = pd.concat([df_employees,df_departments],axis=1)
# print(join)



# join 
join = pd.merge(df_employees ,df_departments , how="outer" , on='dept_id') 
join = join[(join['salary'] >= 80000 ) & (join['dept_name'] == 'IT')]
join['emp_id'] = join['emp_id'].astype('Int64')
# handle missing values
# join['emp_id'] = join['emp_id'].fillna(-1)
# join['name'] = join['name'].fillna('no emp')
# join['dept_name'] = join['dept_name'].fillna('unknown')
# join['salary'] = join["salary"].fillna(0)
# join['location'] = join["location"].fillna('no loc')

join = join.fillna({
    'name' : 'no emp',
    'dept_name': 'Unassigned',
    'location': 'Unknown',
    'salary': 0,
    'emp_id': -1
})
print(join)