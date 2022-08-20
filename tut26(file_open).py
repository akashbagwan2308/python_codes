# Open() Read() And Readline()

f = open('Akash.txt')    # f is a file pointer and open is used to open a file
#print(f.readline())  # will read only one line
content = f.read()   # read() function is used to read a file
print(content)
for line in content:     # it will print line by line
    print(line,end='')
# content = f.read(5)   # this will read only 5 charater
# print('1',content)
# content = f.read(10)   # this will read only 10 charater after 5th
# print('2',content)

f.close()
