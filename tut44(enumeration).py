#enumerate function
list = [ 'Bhindi', 'Aloo', 'Chopstics','Chowmein']
# i = 1
# for item in list:
#     if i%2!=0:
#         print(f'JARVIS please buy {item}')
#     i +=1

for index, item in enumerate(list):   #use of enumerate function
    if index %2 ==0:
        print(f'JARVIS please buy {item}')