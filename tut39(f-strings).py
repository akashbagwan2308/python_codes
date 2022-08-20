# f strings and string functions in python
import math

me = 'Akash'
a1 = 3
 #a = 'This is %s' %me
# a = ' This is {} {}'
# b = a.format(me , a1)
#print(b)
a = f'This is {me} {a1}'  # this is f- string
b = f'This is {me} {a1} {math.cos(65)}'  # this is f- string
print(a)
print(b)
