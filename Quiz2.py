# Quiz 2
print('Enter your age :')
age = int(input())
if 7<age<100:
    if age>18:
        print('You can drive')
    elif age==18:
        print("You are 18 And we can't decide. Please come physically.")
    else:
        print('You can not drive')
else:
    print('Enter a valid age i.e 7<age<100')