#Oops concept
#types of variables
# instance variable
class Student:
    def __init__(self, name, age):
        self.name = name    
        self.age = age      
s1 = Student("hema", 20)
s2 = Student("Anitha", 29)
print(s1.name, s1.age)
print(s2.name, s2.age)

# class variable
class Student2:
    college = "Sridevi"  
    def __init__(self, name):
        self.name = name
s1 = Student2("shreya")
s2 = Student2("ashritha")
print(s1.name, s1.college)
print(s2.name, s2.college)

 # local variable
class Test:
    def show(self):
        x = 100  
        print(x)
t = Test()
t.show()

#types of Methods
#Instance Method
class Student1:
    def __init__(self, name):
        self.name = name
    def display(self):   
        print("Name:", self.name)
s = Student1("devi")
s.display()


#Class Method
class Student:
    college1 = "College"

    @classmethod
    def show_college(cls):
        print("College1:", cls.college1)
Student.show_college()

#ststic method
class Math:
    @staticmethod
    def add(a, b):
        return a + b
print(Math.add(10, 20))
