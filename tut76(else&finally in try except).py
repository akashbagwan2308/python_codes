#  else & finally in try except

f1 = open("Akash.txt")
try:
    f = open("Akash2.txt")
except Exception as e:
    print(e)
else:
    print("This will run only if except is not running")
finally:
    print("Run this anyway... ")
    # f.close()
    f1.close()
print("Important stuff")