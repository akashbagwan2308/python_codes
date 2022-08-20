#classes -- template
# and objects --- instance of the class
#DRY = dont repeat yourself

class Student:   # thiis is class
    pass
Harry = Student()   # this is an object
NArry = Student()   # this is an object

Harry.name = 'HARRY'
Harry.std = 10
Harry.section = 1
NArry.subject = ['Hindi', 'English']
print(Harry.std,NArry.subject)
