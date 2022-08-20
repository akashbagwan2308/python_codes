# generators in python
'''
 Iterable -- __iter__()  or __getitem__()
 Iterator -- __next__()
 Iteration -- it is a process
'''
def gen(n):
    for i in range(n):
        yield i   # yield is a generator

g = gen(3)
print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# k = 58632    integer is not iterable
h = 'harry'    # string is iterable
ite = iter(h)
print(ite.__next__())