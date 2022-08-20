# self , __if__ constructor
class Employee:
    no_of_leaves =8  # class variable
    def __init__(self,Name,Salary,Role):     #constructor
        self.name = Name
        self.salary = Salary
        self.role = Role

    def printdetail(self):  # it is method
        return f'Name is {self.name}. Salary is {self.salary}. Role is {self.role}'



akku = Employee('Akash',4665480,'Instructor') #providing argument to class is known as constructor
jay = Employee('Jay',48668861,'Incharge') #providing argument to class is known as constructor

# akku.name = 'Akash'
# akku.salary = 686865
# akku.role = 'Instructor'
#
# jay.name = 'Jay'
# jay.salary = 646415
# jay.role = 'Incharge'

print(jay.printdetail())
print(akku.printdetail())