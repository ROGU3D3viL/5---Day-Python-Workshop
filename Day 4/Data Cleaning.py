import pandas as pd
df = pd.read_csv("C:/Users/User/OneDrive/Documents/VS Code Documents/Python Workshop For Data Analytics/Study Materials/Projects/Modified_Indian_Employee_Dataset.csv")
print(df.info())
print(df['Salary'])
print(df['Salary'].fillna(df['Salary'].mean(), inplace=True)) # Fill missing values with mean