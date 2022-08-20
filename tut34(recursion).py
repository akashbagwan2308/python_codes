# recursion : recursive and iterative method
# n! = n * n-1 * n-2 * n-3 * ......1
# n! = n * (n-1)!
def factorial_iterative(n):  # this is an iterative approach
    """
     :param n:  Integer
    :return:  n! = n * n-1 * n-2 * n-3 * ......1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
def factorial_recursive(n):  # this is an recursive approach
    """
     :param n:  Integer
    :return:  n! = n * n-1 * n-2 * n-3 * ......1
    """
    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)


num = int(input('Enter the number :'))
print('Factorial using iterative method :',factorial_iterative(num))
print('Factorial using recursive method :',factorial_recursive(num))