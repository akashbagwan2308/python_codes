# if else and elif statements

var1 = 6
var2 = 56
var3 = int(input())
if var3>var2:
    print('Greater')
elif var3==var2:
    print('Equal')
else:
    print('Lesser')

list1 = [5,7,8]
print(5 in list1)# use of 'in' keyword
if 5 in list1:
    print('Yes it is in list1')
print(15 not in list1)# use of 'not in' keyword
if 15 not in list1:
    print('NO it is not in the list1')
