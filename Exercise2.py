# Exercise2
# design a faulty calculator
# 45*3=555,  56+9=77, 56/6=4
op = input('Enter your operator')
print('Enter 1st number :')
n1 = int(input())
print('Enter 2nd number :')
n2 = int(input())
if op =='+':
    if n1==56 and n2==9:
        print('56+9=77')
    else:
        print(n1,'+',n2,'=',n1 + n2)
elif op == '-':
    print(n1,'-',n2,'=',n1 - n2)
elif op =='*':
    if n1==45 and n2==3:
        print('45*3=555')
    else:
        print(n1,'*',n2,'=',n1 * n2)
elif op =='/':
    if n1==56 and n2==6:
        print('56/6=4')
    else:
        print(n1,'/',n2,'=',n1 / n2)