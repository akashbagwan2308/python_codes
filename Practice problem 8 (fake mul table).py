"""Your function should be able to find out the wrong values
in Rohan’s table and expose Rohan Das as a fraud.
Note: Rohan’s function returns a list of numbers like this
Rohan Das’s Function Input:
rohanMultiplication(6)
Rohan’s function returns this output:
[6, 12, 18, 26, …., 60]
You have to write a function isCorrect(table, number) and return
 the index where rohan’s function is wrong and print it to the
 screen! If the table is correct, your function returns None

"""
# ----------------------------------------------------------------
import random
def rohanMul(n):
    rand = random.randint(0,9)
    l = [i*n for i in range(1,11)]
    l[rand] = l[rand] + random.randint(0,10)
    return l

def isCorrect(l,n):
    for i in range(1,11):
        if l[i-1] != n*i:
            return f"{l[i-1]} is wrong in rohan's table at index {i-1}"



if __name__ == '__main__':
    n = int(input("Enter the no for multiplication table :\n"))
    rohanResult = rohanMul(n)
    print(f"Multiplication table of {n} : {rohanResult}")
    print(isCorrect(rohanResult,n))