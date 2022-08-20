# for loops in python
'''Syntax of for loop is
  for x in range(6):   0 to 5
   for x in range(2,6):   from 2 to 5
   for x in range(2,35,3):   from 2 to 34 with an increment of 3

  '''
list = ['Akash','Jay','Surendra','Harsha']
for item in list:    # to print all the element of list
    print(item)
list1 = [['Akash',5],['Jay',3],['Surendra',6],['Harsha',10]]  # list of list
for item in list1:
    print(item)
for item, lolipop in list1:
    print(item, lolipop)
dict1 = dict(list1)
print(dict1)
for item, lolipop in dict1.items():
    print(item," and lolipop is ",lolipop)