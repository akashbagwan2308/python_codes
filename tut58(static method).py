#static method in python

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

    @classmethod
    def from_str(cls,string):
        return cls(*string.split('-'))

    @staticmethod
    def printgood(string):    # this is static method
        print('This is good ' + string)

akku = Employee('Akash',4665480,'Instructor') #providing argument to class is known as constructor
jay = Employee('Jay',48668861,'Incharge') #providing argument to class is known as constructor
surendra = Employee.from_str('Surendra-549569-Student')

print(surendra.printgood('Akash'))