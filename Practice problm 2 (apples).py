"""
input : harry has n no of apples ,
        minimum no
        maximum no
output : no from min to max are divisor of n or not
"""
n = (input("Enter the no of apples Harry have:\n"))
min = (input("Enter the minimum no :\n"))
max = (input("Enter the maximum no :\n"))
try:
    if int(min) == int(max):
        print(f"It is not a range. Min is equal to Max")
    for i in range(int(min), int(max)+1):
        if int(n) % i == 0:
            print(f"{i} is divisor of {int(n)}")
        else:
            print(f"{i} is not divisor of {int(n)}")
except Exception as e:
    print("Input is not valid.It must be an integer")