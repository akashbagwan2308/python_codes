# Break and continue statements in Python
i = 0
while(True):
    if i+1<5:
        i=i+1
        continue 
    print(i+1 ,end =" ")
    if(i==44):
        break # too stop the loop
    i = i +1