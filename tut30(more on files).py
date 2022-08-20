# Seek() tell() and more on python files
f = open('Akash.txt')
# print(f.tell())  # will tell where(at which character) the file pointer is
print(f.readline())
# print(f.tell())  # will tell where(at which character) the file pointer is
f.seek(10)  # will reset your file pointer to a specific position like here 10th character
print(f.readline())
# print(f.tell())  # will tell where(at which character) the file pointer is
f.close()