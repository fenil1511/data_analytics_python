from operator import index

import pandas as pd

# Employee Dataset
data = [
    {"emp_id": 101, "name": "Fenil", "department": "IT", "salary": 85000, "status": "Active"},
    {"emp_id": 102, "name": "Ankit", "department": "HR", "salary": 62000, "status": "Active"},
    {"emp_id": 103, "name": "Rahul", "department": "IT", "salary": 75000, "status": "On Leave"},
    {"emp_id": 104, "name": "Priya", "department": "Finance", "salary": 90000, "status": "Active"},
    {"emp_id": 105, "name": "Karan", "department": "IT", "salary": 110000, "status": "Active"},
    {"emp_id": 106, "name": "Sonia", "department": "Finance", "salary": 58000, "status": "Resigned"}
]

df = pd.DataFrame(data)

sorted_df = df.sort_values('salary', ascending=False)

print(sorted_df)

# 1. Filter Active Employees
# active_emp = df[df['status'] == 'Active']

# # 2. Derive Metrics
# total_active = len(active_emp)
# total_payroll = active_emp['salary'].sum()
# avg_salary = active_emp['salary'].mean()
# bonous_col = active_emp['bonus'] = active_emp['salary'] * 0.1

# # 3. Print Summary
# print(f"Total Active Employees : {total_active}")
# print(f"Total Active Payroll  : ${total_payroll:,}")
# print(f"Average Active Salary  : ${avg_salary:,.2f}\n")



# # 4. Clean Table Display
# print(active_emp[['emp_id', 'name', 'department', 'salary','bonus']].to_string(index=False))

# change_name = df.loc[0,'name'] = ['jay']
# print(df[['emp_id', 'name', 'salary']])