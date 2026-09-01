#Arithemetic Operators
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)
#Assignment Operators
x = 10
x += 5  # x = x + 5
print("Value of x after += 5:", x)
x -= 3  # x = x - 3
print("Value of x after -= 3:", x)
x *= 2  # x = x * 2
print("Value of x after *= 2:", x)
x /= 2  # x = x / 2
print("Value of x after /= 2:", x)
x //= 2  # x = x // 2
print("Value of x after //= 2:", x)
x %= 3  # x = x % 3
print("Value of x after %= 3:", x)
x **= 2  # x = x ** 2
print("Value of x after **= 2:", x)
#Comparison Operators
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)
#Logical Operators
print("Logical AND:", a > 5 and b < 10)
print("Logical OR:", a > 5 or b < 10)
print("Logical NOT:", not(a > 5 and b < 10))
#Bitwise Operators
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)
#Membership Operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True
print(6 not in my_list)  # True
#Identity Operators
y=[1, 2, 3]
z=y
print(y is z)  # True
print(y is not z)  # False
#ternary operator
age = 20
status = "Adult" if age >= 18 else "Not Adult"
print(status)
