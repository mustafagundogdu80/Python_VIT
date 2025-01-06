from functools import reduce
numbers = [1, 2, 3]
print(list(filter(lambda x: (x + 1) * 3 / 3 % 3 == 0, numbers)))
