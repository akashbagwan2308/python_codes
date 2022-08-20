# try except exception in python
print("Enter num 1 :")
num1 = input()
print("Enter num 2 :")
num2 = input()
try:
    print("The sum of num1 andd num2 is :",
      int(num1) + int(num2))   # this line will have error if try except is not used
except Exception as e:
    print(e)
print("This line is very impotant")