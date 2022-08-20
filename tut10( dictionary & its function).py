# dictionary and its functions
# Dictionary is nothing but a key value pairs
d1 = {}
print(type(d1))
d2 = { 'Harry': 'Burger', 'Jay' : 'Capsicum', 'Harsha ' : 'Fish',
       'Surendra': { 'B': 'pohe','L': ' Paneer', 'D':'Maggi'}}
d2['Akash'] = 'Samose'  # can add more element in dictionary
del d2['Akash']  # to  remove the element
print(d2)
print(d2['Surendra']['B'])
d3 = d2.copy()  # to copy the dictionary
print(d3)
d2.update({'Munmun': 'Chocolate'})   # to add or update
print(d2)
print(d2.keys())