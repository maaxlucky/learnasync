import time


def fun1(x):
    print(x ** 2)
    time.sleep(3)
    print('fun1 finished')


def fun2(x):
    print(x ** 0.5)
    time.sleep(3)
    print('fun2 finished')


def main():
    fun1(4)
    fun2(4)


print(type(fun1))

print(type(fun1(4)))
