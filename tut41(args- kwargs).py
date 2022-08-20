# args and kwargs
# def function_name_print(a, b, c, d):
#        print(a, b, c, d)
# function_name_print('Akash', 'Jay', 'Surendra', 'Harsha')
def funargs(normal ,*args ,**kwargs): # it takes multiple arguments
    print(normal)
    for item in args:
        print(item)
    print('\n\nNow I Would Like To Introduce Our Avengers :')
    for key, value in kwargs.items():
        print(f'{key} is {value}')
name = ['Akash','Jay','Surendra','Harsha']
normal = 'I am a normal argument \nFollowing are BE/Btech  students :'
kw = {'Akash': 'Learnig Python','Jay':'Python Expert',
      'Surendra':'Two star coder','Harsha':'Confused about honors 😂 😂 😂'}
# add = input('Enter a new member:\n')
# name.append(add)
funargs(normal,*name,**kw)