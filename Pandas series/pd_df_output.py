Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
=================== RESTART: F:\TECHPANDA\pandasdataframe.py ===================
Emplyee Data:
     Name  Age  Salary Department
0  Samuel   30   39500     Non-IT
1  Sanjay   26   35500         IT
2     Dev   22   28000         HR
3   Aryan   35   50350      Admin

Shape:(4, 4)
----------------------------
First 1 rows only:
     Name  Age  Salary Department
0  Samuel   30   39500     Non-IT
----------------------------
Last 3 rows
     Name  Age  Salary Department
1  Sanjay   26   35500         IT
2     Dev   22   28000         HR
3   Aryan   35   50350      Admin
----------------------------
Statistical Summary:
             Age        Salary
count   4.000000      4.000000
mean   28.250000  38337.500000
std     5.560276   9319.636527
min    22.000000  28000.000000
25%    25.000000  33625.000000
50%    28.000000  37500.000000
75%    31.250000  42212.500000
max    35.000000  50350.000000
----------------------------
Particular column in reverse:
Index(['Name', 'Age', 'Salary', 'Department'], dtype='object')
0    Samuel
1    Sanjay
Name: Name, dtype: object
----------------------------
First 2 columns:
Index(['Name', 'Age', 'Salary', 'Department'], dtype='object')
0    Samuel
1    Sanjay
Name: Name, dtype: object
----------------------------
First 2 columns with Names and Salaries:
Names and Salaries:
     Name  Salary
0  Samuel   39500
1  Sanjay   35500
2     Dev   28000
3   Aryan   50350
----------------------------
Particular row and column:

Row at index 1:
Name          Sanjay
Age               26
Salary         35500
Department        IT
Name: 1, dtype: object
----------------------------

Specific cell - Dulquer's Salary:
39500
----------------------------

First 3 rows:
     Name  Age  Salary Department
0  Samuel   30   39500     Non-IT
1  Sanjay   26   35500         IT
2     Dev   22   28000         HR
----------------------------

Specific cell - row 0,column 2(salary):
39500
----------------------------
     Name  Age  Salary Department
0  Samuel   30   39500     Non-IT
1  Sanjay   26   35500         IT
2     Dev   22   28000         HR
3   Aryan   35   50350      Admin
----------------------------
All IT Department Employees:
     Name  Age  Salary Department
1  Sanjay   26   35500         IT
----------------------------
Employees earning more than 25000:
     Name  Age  Salary Department
0  Samuel   30   39500     Non-IT
1  Sanjay   26   35500         IT
2     Dev   22   28000         HR
3   Aryan   35   50350      Admin
----------------------------
HR employees earning more than 25000:
  Name  Age  Salary Department
2  Dev   22   28000         HR
