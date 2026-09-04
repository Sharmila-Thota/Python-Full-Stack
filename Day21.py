#Generators
def numbers():
    yield 1
    yield 2
    yield 3
for i in numbers():
    print(i)


def numbers(n):
    for i in range(1, n + 1):
        yield i
for x in numbers(5):
    print(x)


def squares(n):
    for i in range(1, n + 1):
        yield i * i
for x in squares(5):
    print(x)

#List comprehension
#Create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

#convert strings to uppercase
words = ["apple", "banana", "cherry"]
uppercase = [word.upper() for word in words]
print(uppercase)

#filter names starting with 'A'
names = ["Alice", "Bob", "Andrew", "Charlie"]
a_names = [name for name in names if name.startswith("A")]
print(a_names)

#Create pairs using nested loops
pairs = [(x, y) for x in [1, 2] for y in ['a', 'b']]
print(pairs)