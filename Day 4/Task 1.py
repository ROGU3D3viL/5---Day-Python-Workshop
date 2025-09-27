import pandas as pd
df = pd.read_csv(input("Enter the file path: ")) # Prompt user for file path
if df is not None:
    print("DataFrame loaded successfully!")
    print("What do you want to do with the DataFrame?\n1. View shape\n2. View columns\n3. Describe the DataFrame\n4. View info")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        print("Shape of the DataFrame:", df.shape)
    elif choice == '2':
        print("Columns of the DataFrame:", df.columns)
    elif choice == '3':
        print("Description of the DataFrame:\n", df.describe())
    elif choice == '4':
        print("Info of the DataFrame:\n", df.info())
    else:
        print("Invalid choice!")
else:
    print("Failed to load the DataFrame.")