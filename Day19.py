#Lambda function
add = lambda a, b: a + b
print(add(10, 20))

#map()
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * x, numbers))
print(result)

#Filter()
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

#reduce()
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a + b, numbers)
print(result)

