# python lists and list function
grocery = ['Harpic','Soap','deodrant','Bhindi','Lolypop',56 ] # this is a list
print(grocery[0])
print(grocery[2])
numbers = [7,5,8,2,6]
#numbers.sort()
#numbers.reverse()
print(numbers[2])
print(numbers[0:5]) # it will take the whole string
print(numbers[1:4])  # it will skip first and last element
print(numbers[::2]) # it skips one elememt
print(max(numbers)) # to find the maximum of the list
print(min(numbers)) # to find the minimum of the list
numbers.append(55)  # to add the element in last of the list
numbers.insert(2, 17)  # will insert the element at index 2
#numbers.remove(8) # it will remove 8
#numbers.pop() # it will remove the elemnent from last
# Mutable == can change
#Immutable == cannat change
tp = (1 ,2,5)
print(tp)
# tp[1] = 6    tuple is immutable
a = 5
b = 8
print(a,b)
a,b = b,a  # to swap the values 
print(a,b)



