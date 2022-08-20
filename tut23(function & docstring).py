# functions and docstrings
a = 9
b = 8
c = sum((a,b))
print(c)

def function():
    print('Hello you are in function ')

function()
function()
function()
def function1(a ,b):
    print('Hello you are in function1 ',a+b)
function1(5 , 7)
def function2(a, b):
    """This function will calculate the average of two numbers"""
    average = (a+b)/2
    print(average)
    return average
v = function2(12,15)
print(v)
print(function2.__doc__)