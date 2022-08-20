"""
Palindromify the list
print next palindrom number onlu if it is greater than 10
input : list = [1,6,87,43]
output : palindromy list = [1,6,88,44]
"""
def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':

    t = int(input("Enter the size of list:\n"))
    numbers=[]
    list = []
    for i in range(t):
        number = int(input("Enter the number for next palindrome:\n"))
        numbers.append(number)
    print("Original list :",numbers)
    print(f"Palindromyfied list : {[numbers[i] if numbers[i]<10 else next_palindrome(numbers[i]) for i in range(t)] }")
    for i in range(t):
        x= int(numbers[i])
        if x >10:
            list.append(next_palindrome(numbers[i]))
        else:
            list.append(x)
            continue
    print("Palindromyfied list :",list)