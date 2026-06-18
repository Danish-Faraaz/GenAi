Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
========== RESTART: F:/TECHPANDA/Pandas series/pandas_series_fillna.py =========
Employee Data:
      Name  Age  Salary Department
0   Samuel   30   39500     Non-IT
1   Sanjay   26   35500         IT
2      Dev   22   28000         HR
3    Aryan   35   50350      Admin
4  Dulquer   40   55000    Manager

Shape: (5, 4)
----------------------
EMPLOYEES SORTED BY AGE (young to old):
      Name  Age  Salary Department
2      Dev   22   28000         HR
1   Sanjay   26   35500         IT
0   Samuel   30   39500     Non-IT
3    Aryan   35   50350      Admin
4  Dulquer   40   55000    Manager
----------------------
EMPLOYEES SORTED BY AGE (old to young):
      Name  Age  Salary Department
4  Dulquer   40   55000    Manager
3    Aryan   35   50350      Admin
0   Samuel   30   39500     Non-IT
1   Sanjay   26   35500         IT
2      Dev   22   28000         HR
----------------------
Sort by Department,then by Salary(highest first):
      Name  Age  Salary Department
3    Aryan   35   50350      Admin
2      Dev   22   28000         HR
1   Sanjay   26   35500         IT
4  Dulquer   40   55000    Manager
0   Samuel   30   39500     Non-IT
----------------------
Age Statistics:
Average Age:30.60
Median Age:30.0
Minimum Age:22
Maximum Age:40
Standard Deviation:7.13
Sum of all Ages: 153
----------------------

After adding Slary_dollar colum:
      Name  Salary  Salary_dollar
0   Samuel   39500     420.212766
1   Sanjay   35500     377.659574
2      Dev   28000     297.872340
3    Aryan   50350     535.638298
4  Dulquer   55000     585.106383
----------------------
After adding Bonus column:
      Name Department  Bonus
0   Samuel     Non-IT   3000
1   Sanjay         IT   6000
2      Dev         HR   5000
3    Aryan      Admin   3000
4  Dulquer    Manager   3000
-----------------------
Average Salary by Department:
Department
Admin      50350.0
HR         28000.0
IT         35500.0
Manager    55000.0
Non-IT     39500.0
Name: Salary, dtype: float64

Type: <class 'pandas.core.series.Series'>
-----------------------
Number of employees per Department:
Department
Admin      1
HR         1
IT         1
Manager    1
Non-IT     1
dtype: int64
-----------------------
Salary Statistics per Department:
               mean    min    max  count
Department                              
Admin       50350.0  50350  50350      1
HR          28000.0  28000  28000      1
IT          35500.0  35500  35500      1
Manager     55000.0  55000  55000      1
Non-IT      39500.0  39500  39500      1
-----------------------
DataFrame with Missing Values:
      Name   Age   Salary Department
0   Samuel  30.0  39500.0        NaN
1   Sanjay  26.0  35500.0         IT
2      Dev   NaN  28000.0         HR
3    Aryan  35.0      NaN      Admin
4  Dulquer  40.0  55000.0    Manager
-------------------------

Missing values count per column:
Name          0
Age           1
Salary        1
Department    1
dtype: int64
-------------------------
Rows with any missing value:
     Name   Age   Salary Department
0  Samuel  30.0  39500.0        NaN
2     Dev   NaN  28000.0         HR
3   Aryan  35.0      NaN      Admin
-------------------------

Rows without any missing value:
      Name   Age   Salary Department
1   Sanjay  26.0  35500.0         IT
4  Dulquer  40.0  55000.0    Manager
-------------------------
Remove rows with missinig values
Original shape:(5, 4)
After dropna():(2, 4)

Cleaned DataFrame:
      Name   Age   Salary Department
1   Sanjay  26.0  35500.0         IT
4  Dulquer  40.0  55000.0    Manager
-------------------------
Fill missing values

After filling missing values:
      Name    Age   Salary Department
0   Samuel  30.00  39500.0         --
1   Sanjay  26.00  35500.0         IT
2      Dev  32.75  28000.0         HR
3    Aryan  35.00      0.0      Admin
4  Dulquer  40.00  55000.0    Manager
-------------------------
Forward fill

Warning (from warnings module):
  File "F:/TECHPANDA/Pandas series/pandas_series_fillna.py", line 111
    df_clean3.fillna(method='ffill',inplace=True)
FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.

After forward fill:
      Name   Age   Salary Department
0   Samuel  30.0  39500.0        NaN
1   Sanjay  26.0  35500.0         IT
2      Dev  26.0  28000.0         HR
3    Aryan  35.0  28000.0      Admin
4  Dulquer  40.0  55000.0    Manager
------------------------
Original DataFrame:
      Name  Age  Salary Department
0   Samuel   30   39500     Non-IT
1   Sanjay   26   35500         IT
2      Dev   22   28000         HR
3    Aryan   35   50350      Admin
4  Dulquer   40   55000    Manager

Columns:['Name', 'Age', 'Salary', 'Department']
------------------------
After adding Experience column:
      Name  Age  Salary Department  Experience
0   Samuel   30   39500     Non-IT           7
1   Sanjay   26   35500         IT           9
2      Dev   22   28000         HR           5
3    Aryan   35   50350      Admin          12
4  Dulquer   40   55000    Manager          15
------------------------
Original columns: ['Name', 'Age', 'Salary', 'Department', 'Experience']

After dropping.Experience column:
      Name  Age  Salary Department
0   Samuel   30   39500     Non-IT
1   Sanjay   26   35500         IT
2      Dev   22   28000         HR
3    Aryan   35   50350      Admin
4  Dulquer   40   55000    Manager
Columns: ['Name', 'Age', 'Salary', 'Department']
------------------------
After dropping Age and Experience columns:
      Name  Salary Department
0   Samuel   39500     Non-IT
1   Sanjay   35500         IT
2      Dev   28000         HR
3    Aryan   50350      Admin
4  Dulquer   55000    Manager
columns: ['Name', 'Salary', 'Department']
