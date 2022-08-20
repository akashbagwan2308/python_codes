print('Total NO of Guesses are 10')
i=1
while(i<=10):
    num = int(input('Enter your number \n'))
    if num == 18:
        print('You Win')
        print('No of guesses you took to finish : ',i)
        break
    elif num<18:
        print('Nah!! Please increase your number')
        print('NO of guesses left : ',10-i)
        if 10-i ==0:
            print('Game Over')
        i = i + 1
        continue
    elif num>18:
        print('Nah!! Please decrease your number')
        print('NO of guesses left : ',10-i)
        if 10-i ==0:
            print('Game Over')
        i = i + 1
        continue
