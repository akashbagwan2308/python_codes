# string slicing and other function in python
mystr = 'Akash is a good boy'
print(len(mystr))
print(mystr[4])  # it takes the element of index 4
print(mystr[0:4]) # it takes the element from index 0 to 3
print(mystr[0:18])
print(mystr[:4]) # it takes the element from index 0 to 3
print(mystr[0:]) # it takes the element from index 0 to available
print(mystr[0:5:2]) # it skips one character
print(mystr[-5:-2]) #it count the index from last
print(mystr[14:17])
print(mystr[::-2])
print(mystr[::-1]) # to reverse the string
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith('boy'))
print(mystr.count('o')) # count the number of o in string
print(mystr.capitalize()) #  to capitalize the string
print(mystr.upper()) # to capitalize each letter
print(mystr.find('is'))
print(mystr.replace('is','are'))