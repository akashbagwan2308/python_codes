# Variables, Datatypes and Typecasting
# variable
var1 = 'Hello world'
var2 = 4
var3 = 36.7
var4 = ' Akash'
var5 = '54'  # here this number is string not a integer
var6 = '36'  # here this number is string not a integer
print(var1)
print(type(var1))    # determining the type of variable
print(type(var2))
print(type(var3))
print(var2 + var3)    #addition of int and float
print(var1+var4)    # addition of two strings
print(var5 + var6)  # addition of two strings
'''Typecasting Functions :
int()
str()
float()
'''
print(int(var5) + int(var6))  # addition of two integers  this is known as typecasting
print(10* 'Hello World ') # 10 times printing of string
print('Enter your number:')
inpnum = input()   # it take input but as a string
print(' Your Number is ', inpnum)