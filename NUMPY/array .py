from array import *
arr1 = array('i',[2,4,6,8])
for m in arr1:
    print(m)
arr2 = array(arr1.typecode,[ a*a for a in arr1])
for n in arr2:
    print(n)
print("GETING ARRAY INPUT")
arr3 = array('i',[])
n = int(input("enter array length"))
b = 0
for b in range(n):
    c = int(input("enter next value"))
    arr3.append(c)
b = b+1
print(arr3)