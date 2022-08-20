#multiple inheritance

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

class Player:
    no_of_games = 8
    def __init__(self,name,game):
        self.name = name
        self.game = game
    def printdetails(self):
        return f'The name is {self.name}. The game is {self.game}'
class CoolProgrammer(Employee,Player):
    language = 'C++'
    def printlanguage(self):
        print(self.language)

akku = Employee('Akash',4665480,'Instructor') #providing argument to class is known as constructor
jay = Employee('Jay',48668861,'Incharge') #providing argument to class is known as constructor

thor = Player('Thor ', ['Cricket'])
captain = CoolProgrammer('Captain America',965921, 'CoolCaptain')
print(captain.printdetail())
captain.printlanguage()
