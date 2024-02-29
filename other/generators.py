
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# for value in simpleGeneratorFun():
#     print(value) // 1 2 3

# x is generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next

# print(next(x)) // 1
# print(next(x))  // 2
# print(next(x)) // 3


# generator for fibonacci numbers
def fib(limit):
    # initialize first two fibonacci numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a+b

y = fib(5)

# print(next(y)) // 0
# print(next(y)) // 1
# print(next(y)) // 1
# print(next(y)) // 2
# print(next(y)) // 3

# print('\nUsing for in loop')
# for i in fib(5):
    # generator is iterable
    # print(i) // same as generator object

# generator expression
generator_exp = (i * 5 for i in range(5) if i%2==0)

for i in generator_exp:
    print(i)




# list comprehension
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, [x for x in numbers]))
# print(squared)