# numpy and array
import numpy as np

new_arr = np.array([1,2,3,4,5])
print(new_arr)
print(np.__version__)
print(type(new_arr))
# creating array using tuple
another_arr = np.array((1,2,3,5,9))
print(another_arr)
# 0- Dimension array
arr = np.array(30)
print(arr)
# 1- D Array
arr1 = np.array([1,2,3,4,5])
print(arr1)
# 2- D Array
arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2)
# 3- D Array
arr3 = np.array([[[1,5,4],[7,8,9]],[[4,8,7],[7,8,9]]])
print(arr3)
# check number of dimensions
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
# Higher dimension array
Arr = np.array([1,2,5,8,7],ndmin =5)
print(Arr)
print('The dimension of array :',Arr.ndim)
# Array indexing
Arr2 = np.array([10,20,54,87])
print(Arr2[0])
print(Arr2[1])
print(Arr2[2])
# Access 2-D array
newArr = np.array([[12,21,23],[54,45,69]])
print("The second element in 1st dim is:",newArr[0,1])
print("The second element in 2nd dim is:",newArr[1,1])
arr3 = np.array([[[1,5,4],[7,8,9]],[[4,8,7],[7,8,9]]])
print('3rd element in 2nd array of 1st array :',arr3[0,1,2])
# array slicing of 1-D array
a = np.array([10,5,2,4,8,6,2,7])
print(a[2:6]) # from index 2 to index 5
print(a[:6]) # from index 0 to index 5
print(a[2:]) # from index 2 to index last
print(a[:-3]) # from index 0 to index last -4
print(a[::-1]) # from index -1 to index 0  i.e reverse of array
print(a[2:7:2]) # from index 2 to index 6 with escaping 1 elements
# 2-D arrat slicing
b = np.array([[1,5,8,7,5,7],[5,7,80,4,3,5]])
print(b[1, 1:4]) # element of 2nd array from index 1 to 3
print(b[0, 1:4]) # element of 1st array from index 1 to 3
print(b[0:2, 2]) # element at index 2 of 1st and 2nd  array
print(b[0:2, 1:4]) # element from index 1  to index 3 of 1st and 2nd  array
# to find the data type in numpy
int = np.array([1,2,5,48])
str = np.array(['banana','tea','apple'],dtype= 'S')
print(int.dtype)
print(str.dtype)
bool = np.array([True,False])
print(bool.dtype)
# Mathematical operation using numpy array
a= np.array([1,2,3,6])
b = a +2
print(b)
b = a -2
print(b)
b = a *2
print(b)
b = a / 2
print(b)
b = np.array([1,2,5,4])
c = a*b
print(c)
d = np.dot(a,b)  #dot product
print(d)
c = np.exp(a) # elements as power of e
print(c)