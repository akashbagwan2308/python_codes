# map filter and reduce function in python
numbers = ['25', '550','56']
numbers = list(map(int,numbers))    # map function is used to type cast list

# for i in range(len(numbers)):
#     numbers[i]= int(numbers[i])
# ---------------------------map function------------------------------
numbers[2] = numbers[2]+1
# print(numbers[2])
# def sq(a):
#     return a*a
# num = [2,5,7,66,44,88,21,45,64]
# square = list(map(sq, num))    # map function is used to apply
#                                 # one unique operation to list
# print('Using sq :\n',square)
#
# num = [2,5,7,66,44,88,21,45,64]
# square = list(map(lambda x:x*x, num))    # map function is used to apply
#                                 # one unique operation to list
# print('Using lambda :\n',square)
# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func = [square, cube]
# for i in range(6):
#     val = list(map(lambda x:x(i), func))
#     print(val)

# -----------------------------filter function-----------------------------------
list1 = [1,2,3,4,5,6,7,8,9]
def is_greater_5(num):
    return num>5
gr_than = list(filter(is_greater_5, list1))
print(gr_than)
# ---------------------------reduce function------------------------------------
from functools import reduce

list2 = [1,2,3,4,5]
n1 = reduce(lambda x,y : x+y, list2)
# n1 = 0
# for i in list2:
#     n1 = n1 + i
print(n1)