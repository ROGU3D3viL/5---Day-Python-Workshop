import pandas as pd
df = pd.read_csv("C:/Users/User/OneDrive/Documents/VS Code Documents/Python Workshop For Data Analytics/Assignments/Assignment Questions & Resources/Resource (Day 4) Modified Indian Employee Dataset.csv") # Read the csv file
print(df) # Print the dataframe
print(df.head(5)) # First 5 rows of the dataframe
print(df.tail(5)) # Last 5 rows of the dataframe
print(df.shape) # (rows, columns) of the dataframe
print(df.columns) # Column names of the dataframe
print(df.info()) # Concise summary of the dataframe
print(df.describe()) # Statistical summary of the dataframe
print(df.groupby('City').agg({'City': 'count'})) # Count of employees in each city