# if __name__ ==__main__ usage and necessity


def printhar(string):
    return f'Ye string harry ko de de thakur {string}'

def add (num1, num2):
    return num1+num2+5
print('And the name is ',__name__)
if __name__ == '__main__':      #  to avoid the extra content of this file after import in any file :: we use
    # if__name__ = '__main__'
    print(printhar('Harry1'))
    o = add(4,5)
    print(o)