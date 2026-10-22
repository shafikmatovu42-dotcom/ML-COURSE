from numpy import *
num = linspace(0,14,5,)
print(num)

print("LOGSPACE")
log = logspace(1,10,5)
print(log)
"""THIS IS DEEP COPY AND 
    SHALLOW COPY"""
print("shallow copy")
arr1 = array([5,4,3,2,1])
arr2 = arr1.view()
arr2[1] = 9
print(arr1)
print(arr2)
print("then for deep copy")
arr1 = array([5,4,3,2,6,1])
arr2 = arr1.copy()
arr2[1] = 9
print(arr1)
print(arr2)
print("2D array in arrays")
arr1 = array([
    [3,2,1],
    [7,4,9]
           ])
print(arr1)
print(arr1.flatten)
print("then for MATRICES")
b = matrix(arr1)
c = matrix(arr2)
print(arr1)
arr3 = arr2.reshape[3,3]
print(arr3)
