#  operator overloading And dunder method
#  Dunder Method = a method sartint and ending with __


class Employee:
    no_of_leaves =8  # class variable
    def __init__(self,Name,Salary,Role):
        self.name = Name
        self.salary = Salary
        self.role = Role

    def printdetail(self):  # it is method
        return f'Name is {self.name}. Salary is {self.salary}. Role is {self.role}'
    @classmethod
    def change_leave(cls,newleaves):    # class method
        cls.no_of_leaves =newleaves
    def __add__(self, other):   # this is a dunder method ,it is made only to perform (emp1+emp2)
        # and this is helping in operator overloading
        return self.salary +other.salary
    def __truediv__(self, other):
        return self.salary /other.salary
    def __repr__(self):
        return f'Employee("{self.name}", {self.salary}, "{self.role}")'
    def __str__(self):
        return f'Name is {self.name}. Salary is {self.salary}. Role is {self.role}'


emp1 = Employee('Akash',2518,'Programmer')
emp2 = Employee('Jay',951,'Student')
print(emp1+emp2)
print(emp1/emp2)
print(emp1)