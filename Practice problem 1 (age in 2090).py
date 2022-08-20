#  Practice problem 1
# Your age in 2090
"""
Take input from user i.e  age or year of birth
And tell them when will they turn 100 years old
take the input as year ,which will tell their age in that year
Also handle the error, like:
1. You are not yet born
2. You seems to be oldest person alive
"""
# ----------------------------------------------------------------------------------------------- #
future = 2090
present = 2022

def Agecalc(age):
    if age>present:
        return "You are not born yet"
    elif age > 140:
        return future - age
    else:
        return future - present + age
def century(age):
    if age>present:
        return "You are not born yet"
    elif age > 140:
        return 100 + age
    else:
        return present + 100 - age
def agepredictor(year):
    if age > 140:
        return year - age
    else:
        return year - present + age

if __name__ == '__main__':
     while(True):
        age = int(input("Enter your age/year of birth :\n"))
        print(f"Your age will be {Agecalc(age)} years in 2090")
        print(f"You will be of 100 years in year{century(age)}")
        year = int(input("Enter the year for which you want your age :\n"))
        print(f"You will be of {agepredictor(year)} years in year {year}")

        print("Press q to quit and c to continue")
        user_choise2 = ""
        while (user_choise2 != "c" and user_choise2 != "q"):
            user_choise2 = input()
            if user_choise2 == "q":
                exit()
            if user_choise2 == "c":
                continue