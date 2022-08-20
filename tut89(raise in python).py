# Raise in Python

a = input("What is your name ??\n")
b = input("How much do you earn\n")
if int(b)==0:
    raise ZeroDivisionError("B is zero so stopping the program")
if a.isnumeric():
    raise Exception("Numers are not allowed")
print(f"Hello!! {a} \nYour salary is {b}")
#1000 lines taking 1 hour

# -------------try except----------

c = input("Enter your name ")
try:
    print(z)
except Exception as e:
    if c == "harry":
        raise ValueError("Harry is blocked he is not allowed")
    print("Exception Handled")