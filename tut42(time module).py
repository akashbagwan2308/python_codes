# time module in python
import time

initial = time.time()
print(initial)
k = 0
while(k<5):
    print('I am a good boy')
    time.sleep(2)      # to stop the time for 2 seconds
    k+=1
print("While loop ran in :", time.time()-initial,'seconds')
initial1 = time.time()
for i in range(5):
     print('I am a good boy')
     time.sleep(2)   # to stop the time for 2 seconds
print("For loop ran in :", time.time()-initial1,'seconds')
localtime = time.asctime(time.localtime(time.time()))
print(localtime)