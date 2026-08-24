import pandas as  pd
data = [
    {"emp_id": 101, "name": "Fenil", "department": "IT", "salary": 85000, "status": "Active", "doj": "2022-01-15"},
    {"emp_id": 102, "name": "Ankit", "department": "HR", "salary": 62000, "status": "Active", "doj": "2021-06-20"},
    {"emp_id": 103, "name": "Rahul", "department": "IT", "salary": 75000, "status": "On Leave", "doj": "2023-03-10"},
    {"emp_id": 104, "name": "Priya", "department": "Finance", "salary": 90000, "status": "Active", "doj": "2020-11-01"},
    {"emp_id": 105, "name": "Karan", "department": "IT", "salary": 110000, "status": "Active", "doj": "2019-08-05"},
    {"emp_id": 106, "name": "Sonia", "department": "Finance", "salary": 58000, "status": "Resigned", "doj": "2022-09-12"}
]

df = pd.DataFrame(data)



# change data type str to date
df['doj'] = pd.to_datetime(df['doj'])
df['month']=df['doj'].dt.strftime('%b')
df['year']=df['doj'].dt.year
print(df)
