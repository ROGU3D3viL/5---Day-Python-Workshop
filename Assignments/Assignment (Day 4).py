import pandas as pd
df1 = pd.DataFrame({'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                   'Liters': [10, 12, 9, 11, 13, 8, 4]})
print(df1.head(3)) # First 3 rows of the dataframe
print(df1.shape) # (rows, columns) of the dataframe
print(df1.columns) # Column names of the dataframe
print(df1.dtypes) # Data types of the columns)


df2 = pd.DataFrame({'Category' : ['Rent', 'Food', 'Utilities', 'Transport'],
                   'Amount' : [15000, 8000, 2000, 3000]})
print(df2)
print(df2['Amount'].agg(['sum', 'mean', 'max', 'min'])) # Sum, mean, max, min of the Amount column