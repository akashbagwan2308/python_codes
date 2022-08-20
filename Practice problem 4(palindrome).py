"""
a palindrome is a string which is equal to its revers
i.e 6116 = 6116, 616 = 616,MOM = MOM, POP=POP
input: no of test cases, and then numbers
        3
        10
        412
        2133
output: Next palindrome for 10 is 11
        Next palindrome for 412 is 414
        Next palindrome for 2133 is 2222
"""
def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':

    t = int(input("Enter the no of testcases:\n"))
    numbers=[]
    for i in range(t):
        number = int(input("Enter the number for next palindrome:\n"))
        numbers.append(number)

    for i in range(t):
            print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
