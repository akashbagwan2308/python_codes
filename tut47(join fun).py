#join function in python
list = [ 'Captain America','Thor Odinson', 'Natasha Romanhoff',
         'Agent Barton', 'Jane Froster', 'Peggi Carter',
         'Peter Parker']
for item in list:
    print(item,'and',end=' ')
print('Other Marvel SuperHeros')
a = ' and '.join(list)       # this join function will work same as for loop
print(a,'and Other Marvel SuperHeros')
a = ' , '.join(list)       # this join function will work same as for loop but join with comma
print(a,', Other Marvel SuperHeros')