#try and Except 
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter numbers only")

#Using else and finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

else:
    print("Result:", result)

finally:
    print("Program completed")

