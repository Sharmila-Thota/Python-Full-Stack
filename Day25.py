#Inheritance
class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.eat()
d.bark()

#Single Inheritance
class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
c = Car()
c.start()
c.drive()

#Multiple Inheritance
class Father:
    def skills(self):
        print("Father knows driving")
class Mother:
    def talent(self):
        print("Mother knows cooking")
class Child(Father, Mother):
    def play(self):
        print("Child plays cricket")
c = Child()
c.skills()
c.talent()
c.play()

#Multilevel Inheritance
class Person:
    def introduce(self):
        print("I am a person")
class Employee(Person):
    def work(self):
        print("Employee is working")
class Manager(Employee):
    def manage(self):
        print("Manager manages the team")
m = Manager()
m.introduce()
m.work()
m.manage()

#Hierarchical Inheritance
class Shape:

    def display(self):
        print("This is a shape")


class Circle(Shape):

    def area(self):
        print("Area of circle")


class Rectangle(Shape):

    def area(self):
        print("Area of rectangle")


c = Circle()
r = Rectangle()

c.display()
c.area()

r.display()
r.area()

#Hybrid Inheritance
class Person:
    def name(self):
        print("Person has a name")
class Student(Person):
    def study(self):
        print("Student studies")
class Teacher(Person):
    def teach(self):
        print("Teacher teaches")
class Assistant(Student, Teacher):
    def help(self):
        print("Assistant helps students")
a = Assistant()
a.name()
a.study()
a.teach()
a.help()

#Access Modifiers
#Public
class Student:
    def __init__(self):
        self.name = "ani"

s = Student()

print(s.name)

#Protected
class Student:
    def __init__(self):
        self._name = "Sharmila"

class College(Student):
    def display(self):
        print(self._name)

c = College()
c.display()

#Private
class Student:
    def __init__(self):
        self.__marks = 90

    def display(self):
        print(self.__marks)

s = Student()
s.display()



    