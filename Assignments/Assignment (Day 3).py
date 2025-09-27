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


i = input("Enter icon: ")
if i.isdigit():
    arr3 = np.full((7,5), int(i))
    print(np.shape(arr3))
    print(arr3)
else:
    arr3 = np.full((9,4),i)
    print(np.shape(arr3))
    print(arr3)


arr4 = np.array([1, 2, 3, 4, 5])
print(np.ndim(arr4))


num = []
for i in range(4):
    n = int(input(f"Enter number {i+1}: "))
    num.append(n)
arr5 = np.array([num])
print(np.dtype(arr5))


num1 = int(input("Enter number of elements: "))
num = []
for i in range(num1):
    n = int(input(f"Enter number {i+1}: "))
    num.append(n)
arr6 = np.array([num])
print(np.astype(arr6, float))


