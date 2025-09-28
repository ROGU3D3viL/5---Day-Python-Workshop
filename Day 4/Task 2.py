import pandas as pd
df = pd.DataFrame({'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                   'Liters': [10, 12, 9, 11, 13, 8, 4]})
print(df.head(3)) # First 3 rows of the dataframe
print(df.shape) # (rows, columns) of the dataframe
print(df.columns) # Column names of the dataframe
print(df.dtypes) # Data types of the columns)