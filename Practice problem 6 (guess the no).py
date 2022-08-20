"""
Generate a random integer from a to b. You and your friend have to guess a
number between two numbers,a and b. a and b are inputs taken from the user.
Your friend is player 1 and plays first. He will have to keep choosing the
number, and your program must tell whether the number is greater than the
actual number or less than the actual number.
Input:
Enter the value of a 4
Enter the value of b 13
Output:
Player1 :
Please guess the number between 4 and 13
5
Correct, you took 3 trials to guess the number
Player 2:
Correct, you took 7 trials to guess the number
Player 1 wins!
"""
# --------------------------------------------------------------------------------
import random
def playgame(r):
    i = 1
    while (True):
        g = int(input("Guess the number :\n"))
        if g == r:
            print("Congratulations!!! You guess the number correctly.")
            print(f"You took {i} no of trials.")
            break
        elif g > r:
            print("Worng!!! Guess again Lesser.")
            i = i + 1
            continue
        elif g < r:
            print("Worng!!! Guess again Greater.")
            i = i + 1
            continue
    return i
def winner(n1,n2):
    if n1>n2:
        return f"Player 2 is winner."
    elif n1<n2:
        return f"Player 1 is winner."
    else:
        return f"You both are winners."

if __name__ == '__main__':
    a = int(input("Enter the value of a :\n"))
    b = int(input("Enter the value of b :\n"))
    r = random.randint(a,b)
    print(r)
    print(f"Player 1 :\nPlease guess the number betweer {a} and {b}")
    n1 = playgame(r)
    print(f"Player 2 :\nPlease guess the number betweer {a} and {b}")
    n2 = playgame(r)
    print(winner(n1,n2))