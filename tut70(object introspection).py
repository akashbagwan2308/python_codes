# object introspection

class Employee:
    def __init__(self,fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"    To avoid no change result ,setter is used
    def explain(self):
        return f"The employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return 'Email is not set. Please set it using setter'
        return f"{self.fname}.{self.lname}@codewithharry.com"
    @email.setter
    def email(self, string):
        print("Setting Now....")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname =None
        self.lname = None
skillf = Employee('Skill','F')
# print(skillf.email)

print(type(skillf))    # by finding the type , i am doing th object introspection
print(type('This is a string'))
print(id('This is a string'))
print(id('This is an string'))
print(dir('This is an string'))

import inspect

print(inspect.getmembers(skillf))