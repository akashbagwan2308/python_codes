# Scope Global variable and global keyword
l = 10 # global variable
def function(n):
    # l = 5   # local variable
    m = 8
    global l # it is the permission to change the global variable
    l =l +45    #can not change global variable in the absence of local variable
    print(l,m)
    print(n,'I have printed')
function('Yes its me')
print(l)

def harry():
    x = 20
    def rohan():
        global x
        x = 88       # it will check the global variable outside the functions
    print('Before calling rohan()', x)
    rohan()
    print('After calling rohan()', x)
harry()
print(x)