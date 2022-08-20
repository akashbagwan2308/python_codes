l = ['This is good','Python is good','Pyhton is not a pyhton snake']

d = "Python"
d2 = d.lower()
k=0
for i in range(len(l)):
    mystr = str(l[i])
    a = mystr.lower()
    b = a.split(" ")
    for i in range(len(b)):
        if b[i]==d2:
            k=k+1
        # if k>0:
        #     print(b[i])
        if k-1 == 0:
            print(l[i])
