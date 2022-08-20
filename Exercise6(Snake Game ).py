# Snake water gun
# 1. snake - water = snake
# 2. water - gun = water
# 3. gun - snake = gun
# total attemt 10
# no of time of winnig
import random
list = [ 'SNAKE','WATER','GUN']
k = 0
m = 0
i = 0
# total no of attempt is 10
while(i<=10):
 pr2 = random.choice(list)  # person2
 pr1 = input('Enter your choice :\n')  # person1
 if 'SNAKE' == pr1 and 'WATER' == pr2 :
  print('YOU WIN')
  print('EXCELLENT! ONCE MORE')
  k = k + 1
  i = i+1
 elif 'WATER' == pr1 and 'GUN' == pr2:
  print('YOU WIN')
  print('EXCELLENT! ONCE MORE')
  k = k + 1
  i = i + 1
 elif 'GUN' == pr1 and 'SNAKE' == pr2:
  print('YOU WIN')
  print('EXCELLENT! ONCE MORE')
  k = k + 1
  i = i + 1
 elif 'SNAKE' == pr2 and 'WATER' == pr1 :
  print('AI WIN')
  print('Try Again ')
  m = m + 1
  i = i+1
 elif 'WATER' == pr2 and 'GUN' == pr1:
  print('AI WIN')
  print('Try Again ')
  m = m + 1
  i = i + 1
 elif 'GUN' == pr2 and 'SNAKE' == pr1:
  print('AI WIN')
  print('Try Again ')
  m = m + 1
  i = i + 1
 else:
  print('Try Again ')
  i = i + 1
if k==1:
 print('You Won 1 Time')
else:
 print('You Won',k,'Times')
if m ==1:
 print('AI Won 1 Time')
else:
 print('AI Won',m,'Times')


