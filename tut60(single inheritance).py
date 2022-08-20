#single inheritance

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

class Programmer(Employee):
    no_of_holidays = 70
    def __init__(self,Name,Salary,Role,Languages):     #constructor
        self.name = Name
        self.salary = Salary
        self.role = Role
        self.languages = Languages

    def printprog(self):
        return f'The Programmers Name is {self.name}. Salary is {self.salary}. Role is {self.role}. Languages are ' \
               f'{self.languages}'

akku = Employee('Akash',4665480,'Instructor') #providing argument to class is known as constructor
jay = Employee('Jay',48668861,'Incharge') #providing argument to class is known as constructor

captain = Programmer('Captain America', 856225 , 'Programmer',['python'])
thor = Programmer('Thor', 651668, 'Programmer',['python','c++'])
print(thor.printprog())
print(thor.no_of_holidays)