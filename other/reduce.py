import functools

# letters = ['H', 'E', 'L', 'L', 'O']
# word = functools.reduce(lambda x, y,: x + y, letters)
# H + E = HE, HE + L = HEL, HEL + L = HELL, HELL+O = HELLO
# print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y,: x * y, factorial)
print(result)