import pandas as pd
df = pd.read_csv("C:/Users/User/OneDrive/Documents/VS Code Documents/Python Workshop For Data Analytics/Study Materials/Projects/Modified_Indian_Employee_Dataset.csv")
print(df) # Print the dataframe
print(df.head(5)) # First 5 rows of the dataframe
print(df.tail(5)) # Last 5 rows of the dataframe
print(df.shape) # (rows, columns) of the dataframe
print(df.columns) # Column names of the dataframe
print(df.info()) # Concise summary of the dataframe
print(df['Name']) # Accessing a specific column