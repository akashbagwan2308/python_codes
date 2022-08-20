# write and appending  and read-write mode to a file
# f = open('Akash2.txt','w')   # w is used to write in file
f = open('Akash2.txt','a')   # a is used to append/add in file
# f.write('\nAkash is a smart boy')
a = f.write('\nAkash is a smart boy')
print(a)  # will show that how much character we have written
f.close()
# Handle read an write both
f = open("Akash2.txt",'r+')  # r+ is used to read and write both in a file
print(f.read())
f.write('\nThank you')
f.close()