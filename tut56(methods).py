#class methods

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


akku = Employee('Akash',4665480,'Instructor') #providing argument to class is known as constructor
jay = Employee('Jay',48668861,'Incharge') #providing argument to class is known as constructor
jay.change_leave(55)
# print(jay.printdetail())
# print(akku.printdetail())
print(jay.no_of_leaves)