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

#for us to change the shape of an array
print("\n for us to change the shape of an array")
print("...........................")

changed_array = my_array.reshape((2,2,3))

print(changed_array)

#creating empty arrays using
"""
np.zeros()
np.ones()
np.empty()

  """
print("\n creating empty arrays using np.zeros()")
print("...........................")

zero_arrray = np.zeros((3,3))
print(zero_arrray)



print("\n creating empty arrays using np.ones()")
print("...........................")

ones_array = np.ones((3,3))
print(ones_array)

print("\n creating empty arrays using np.empty()")
print("...........................")

empty_array = np.empty((3,3))
print(empty_array)
print("\n for np.empty, values change (randomly) basing on the parameters ")


print("\n using np.eye() function")
print("...........................")

eye_array = np.eye(3)
print(eye_array)
print("default main diagonal is 1 and the rest are 0s\n This can be changed by using the k parameter to specify which diagonal to fill with 1s")

print("\n using np.eye() function with k parameter")
print("...........................")

eye_array = np.eye(3, k=1)
print(eye_array)

##manipulating the values of the array:
print("\n we can change the values of the array by using indexing and slicing")
print("............changing the zeros...............")

eye_array[eye_array ==0] = 5
print(eye_array)
print("...........other operations can be used too(+,<,* , etc)...............")

print("\n changing values bassing on RAW/COLUMN")
print("lets change the first raw to 3's")

eye_array[0] = 3
print(eye_array)

print("\n changing the column values to any eg 4")
eye_array[:, 0] = 4
print(eye_array)

print("\n we can also target a specific value")
print("lets change the one in the 2nd raw and 3rd column to 9")

eye_array[1:-1,2:3] = 9
print(eye_array)





