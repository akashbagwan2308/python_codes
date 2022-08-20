# #decortion in pyhton
# def function1():
#     print('Subscribe Now')
#
# func2 = function1
# func2()
#
# def funcret(num):
#      if num==0:
#          return print
#      if num ==1:
#          return sum
# a = funcret(0)
# print(a)
# def executer(fun):
#     fun('This is')
# executer(print)
# ----------------decorator--------------------
def dec1(func1):
    def nowexec():
        print('Executing now')
        func1()
        print('Executed')
    return nowexec
@dec1  # this is a decorator
def who_is_harry():
    print('Harry is a good boy')
# who_is_harry = dec1(who_is_harry)      this is a decorator
who_is_harry()