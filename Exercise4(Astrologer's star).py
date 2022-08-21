# Pattern Printing
n = int(input('Enter desired no. of rows of star \n'))
bool= int(input('Enter boolean no.(0/1) :\n'))
if True == bool:
    i=1
    while(i<=n):
        print(i*"* ")
        i=i+1
elif False == bool:
    while (n):
        print(n * "* ")
        n = n - 1