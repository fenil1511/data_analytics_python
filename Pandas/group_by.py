import pandas as pd

# Sample dataset with missing values (None and pd.NA)
data = [
    {"emp_id": 101, "name": "Fenil", "department": "IT", "salary": 85000, "doj": "2022-01-15"},
    {"emp_id": 102, "name": "Ankit", "department": None, "salary": 62000, "doj": "2021-06-20"},
    {"emp_id": 103, "name": "Rahul", "department": "IT", "salary": pd.NA, "doj": None},
    {"emp_id": 104, "name": "Priya", "department": "Finance", "salary": 90000, "doj": "2020-11-01"},
    {"emp_id": 105, "name": "Karan", "department": None, "salary": 110000, "doj": "2019-08-05"},
    {"emp_id": 106, "name": "Sonia", "department": "Finance", "salary": pd.NA, "doj": "2022-09-12"}
]

df = pd.DataFrame(data)

# convert in datae
df['doj']=pd.to_datetime(df['doj'])
df['month'] = df['doj'].dt.strftime('%b')
# df=df.groupby(['month','department'])['salary'].sum()
# df=df['department'].value_counts()


# Filter and display all IT employees
# it_employees = df[df['department'] == 'IT'].value_counts(dropna=False)
# print(it_employees)
print(df)
# group by 
salary= df.groupby(['department','month']).agg({'salary' : 'sum' , 'name' : 'count' })
tot_salary = salary.sum()
print(salary)

print(tot_salary)