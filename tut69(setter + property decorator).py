#   setter & property decorators

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

akash = Employee("Akash", "Bagwan")
jay = Employee("Jay", "Barode")
# print(jay.explain())
print(jay.email)
jay.fname = 'Thor'
print(jay.email)
jay.email = "Thor.Odinson@codewithharry.com"
print(jay.fname)
print(jay.lname)
print(jay.email)
del jay.email
print(jay.email)
