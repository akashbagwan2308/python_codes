# class method as alternative constructor

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
        # para = string.split('-')
        # return cls(para[0],para[1],para[2])
        return cls(*string.split('-'))
akku = Employee('Akash',4665480,'Instructor') #providing argument to class is known as constructor
jay = Employee('Jay',48668861,'Incharge') #providing argument to class is known as constructor
surendra = Employee.from_str('Surendra-549569-Student')
# jay.change_leave(55)
# print(jay.printdetail())
# print(akku.printdetail())
# print(jay.no_of_leaves)
print(surendra.printdetail())