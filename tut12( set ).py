# set in python
s = set()
s_from_list = set([1,5,8,6,7])
print(type(s))
print(s_from_list)
s.add(4) # set operation to add element in empty set
s.add(3) # set operation to add element in empty set
s1 = s.union({5,9,11,13}) # to find the union of two sets
s.remove(3) # to remove the element 
print(s, s1)
s2 = s.intersection({4,5,6}) # to find the intersection of two sets
print(s2)
