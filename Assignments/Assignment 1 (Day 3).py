import numpy as np
num = []
for i in range(3):
    n = int(input(f"Enter number {i+1}: "))
    num.append(n)

arr1 = np.array(num)
print(arr1)

num = []
for i in range(5):
    n = int(input(f"Enter number {i+1}: "))
    num.append(n)

arr2 = np.array([num])
print(np.size(arr2))

row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
zero_arr = np.zeros((row,col))
print(zero_arr)

row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
one_arr = np.ones((row,col))
print(one_arr)

row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
i = input("Enter icon: ")
if i.isdigit():
    arr3 = np.full((row,col), int(i))
    print(np.shape(arr3))
else:
    arr3 = np.full((row,col),i)
    print(np.shape(arr3))