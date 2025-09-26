# Importing numpy library
import numpy as np

# Creating a numpy array
arr = np.array([1, 2, 3, 4, 5])
for i in range(len(arr)):
    print(arr[i])
print(type(arr))

# Performing operations on numpy multi-dimentional array
arr2 = np.array([[1, 22, 31], [423, 543, 65], [7532, 8, 9]])
print(np.sum(arr2)) # sum of all elements in the array
print(np.min(arr2)) # minimum value in the array
print(np.max(arr2)) # maximum value in the array
print(round(np.mean(arr2),2)) # mean of all elements in the array
print(np.prod(arr2)) # product of all elements in the array

# Making a zero array
zero_arr = np.zeros((2, 3)) # 2 rows and 3 columns
print(zero_arr)

# Making a one array
one_arr = np.ones((2, 3)) # 2 rows and 3 columns
print(one_arr)

# Making a full array
full_arr = np.full((2, 3), 7) # 2 rows and 3 columns with all values as 7
full_arr2 = np.full((2, 3), "Yo!") # 2 rows and 3 columns with all values as "Yo!"
print(full_arr)
print(full_arr2)

# Making a dynamic array
i = int(input("Enter number of rows: "))
j = int(input("Enter number of columns: "))
k = input("Enter default value: ")
if k.isdigit():
    dyn_arr = np.full((i, j), int(k))
    print(dyn_arr)
else:
    print("Invalid input...!")