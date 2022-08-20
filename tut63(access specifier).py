#public ,private ,protected access specifier
class Employee:
    no_of_leaves =8  # class variable
    _protec = 9 # protected
    __private = 100 # private  it can be used in this class only
    def __init__(self,Name,Salary,Role):
        self.name = Name
        self.salary = Salary
        self.role = Role

    def printdetail(self):  # it is method
        return f'Name is {self.name}. Salary is {self.salary}. Role is {self.role}'
    @classmethod
    def change_leave(cls,newleaves):    # class method
        cls.no_of_leaves =newleaves

    @classmethod
    def from_str(cls,string):
        return cls(*string.split('-'))

    @staticmethod
    def printgood(string):    # this is static method
        print('This is good ' + string)

emp = Employee('Jay', 841654, 'Student')
print(emp._protec)
# print(emp.__private)  It will throw an error ,we cant use it directly
print(emp._Employee__private)  # it is done by name labeling 