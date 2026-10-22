import numpy as np

my_array = np.arange(8)       # 8 is our stop value here.

print(my_array)

print("\n the shape of the array")
print('...........................')

print(my_array.shape)

print(type(my_array))

#for a custon range
print("\n for a custon range")
print("...........................")

my_array = np.arange(3 , 10)  # here 8 is our stop value 

#to print only odds or evens    ::: we used 2 a our step value

my_array = np.arange(0,10,2) # this returns only even numbers from our range

print(my_array)

# for us to conver a list to an array

list_2_array = np.array([1,2,3,4,5,6])

print (list_2_array)

#2d arrays

print("\n for 2d arrays") # while using multiple raws
print("...........................")

from_list = np.array([[1,3,2,4],[5,6,7,8]])
print(from_list)

# using the arange and array functions

print("\n for 2d arrays and using the arange and array functions")
print("...........................")

my_array = np.array([np.arange(0,12,2), np.arange(1,12,2)])


print(my_array) 

print("to see the shape of our aray")
