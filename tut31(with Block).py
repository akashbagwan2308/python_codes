# Using with block to open a file
with open('Akash.txt') as f:    # doing same thing as line 3 
    a = f.read()
    print(a)
# #f = open('Akash.txt')
# print(f.readline())
# print(f.readlines())
# f.close()