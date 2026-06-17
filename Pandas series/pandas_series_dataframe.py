import pandas as pd
import numpy as np
data = {'Name':['Samuel','Sanjay','Dev','Aryan'],
    'Age':[30,26,22,35],
    'Salary':[39500,35500,28000,50350],
    'Department':['Non-IT','IT','HR','Admin']}
df = pd.DataFrame(data)
print("Emplyee Data:")
print(df)
print(f"\nShape:{df.shape}")

print("----------------------------")
print("First 1 rows only:")
print(df.head(1))

print("----------------------------")
print("Last 3 rows")
print(df.tail(3))

print("----------------------------")
print("Statistical Summary:")
print(df.describe())

print("----------------------------")
print("Particular column in reverse:")
print(df.columns)
print(df['Name'][:2])

print("----------------------------")
print("First 2 columns:")
print(df.columns)
print(df['Name'][:2])

print("----------------------------")
print("First 2 columns with Names and Salaries:")
print("Names and Salaries:")
print(df[['Name','Salary']])

print("----------------------------")
print("Particular row and column:")
print("\nRow at index 1:")
print(df.loc[1])

print("----------------------------")
print("\nSpecific cell - Dulquer's Salary:")
print(df.loc[0,'Salary'])

print("----------------------------")
print("\nFirst 3 rows:")
print(df.iloc[0:3])

print("----------------------------")
print("\nSpecific cell - row 0,column 2(salary):")
print(df.iloc[0,2])

print("----------------------------")
print(df)

print("----------------------------")
print("All IT Department Employees:")
it_employees =df[df['Department'] == 'IT']
print(it_employees)

print("----------------------------")
print("Employees earning more than 25000:")
high_earners = df[df['Salary']>25000]
print(high_earners)

print("----------------------------")
print("HR employees earning more than 25000:")
filtered = df[(df['Department'] =='HR')&(df['Salary']>20000)]
print(filtered)
