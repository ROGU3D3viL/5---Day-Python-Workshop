import pandas as pd
df = pd.read_csv("C:/Users/User/OneDrive/Documents/VS Code Documents/Python Workshop For Data Analytics/Assignments/Assignment Questions & Resources/Resource (Day 4) Modified Indian Employee Dataset.csv")
print(df.info())
print(df['Salary'])
print(df['Salary'].fillna(df['Salary'].mean(), inplace=True)) # Fill missing values with mean