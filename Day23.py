
#Constructor
class Student:
    def __init__(self):
        print("Constructor called")
s1 = Student()

#Parameterized Constructor
class Student1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = Student1("Sharmila", 22)
print(s1.name)
print(s1.age)

#Non-Parameterized Constructor
class Student:
    def __init__(self):
        self.name = "Sharmila"
        self.age = 22
s1 = Student()
print(s1.name)
print(s1.age)

#Default Constructor
class Student3:
    def __init__(self):
        print("Student object created")
s1 = Student3()
