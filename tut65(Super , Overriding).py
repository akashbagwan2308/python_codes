# Super() & Overriding in classes
class A:
    classvar1 = ' I am a class variable in class A '
    def __init__(self):
        self.var1 = "I am in class A's constructor"
        self.classvar1 = 'Instance var in class A'
        self.special = 'Special'

class B(A):
    classvar1 = 'I am in class B'   # overriding
    def __init__(self):
        super().__init__()    # super class ke constructor ko call kr do
        self.var1 = "I am in class B's constructor"
        self.classvar1 = 'Instance var in class B'
a= A()
b = B()
print(b.special)