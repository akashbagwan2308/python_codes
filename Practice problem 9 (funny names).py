"""
Problem Statement:-
It's result day at school and not everyone is happy. You decided to make
your friends laugh by jumbling their names to come up with some funny names.
Your program should take the number of names and the names separated by space
as input. Output should be funny names in the same order.
Input:
Enter number of friends:
3
Enter the name of your 3 friends:
Rohan Das
Shubham Agarwal
Ritesh Arora
Output:
Ritesh Das
Shubham Arora
Rohan Agarwal
"""
import random
def funny(l1,l2,n):
    for i in range(n):
        print(f"{l1[i]} {random.choice(l2)}")



if __name__ == '__main__':
     n = int(input("Enter the no of your friends :\n"))
     l1 =[]
     l2 =[]
     for i in range(n):
         f,s = input(f"Firend {i+1}:\n").split(" ")
         l1.append(f)
         l2.append(s)
     # print(f"Funny names :\n{funny(l1,l2,n)}")
     funny(l1,l2,n)