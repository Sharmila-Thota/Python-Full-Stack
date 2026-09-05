#Polymorphism
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
d = Dog()
c = Cat()
d.sound()
c.sound()

#Types of polymorphism
#Method Overloading
class Calculator:
    def add(self, *numbers):
        total = 0
        for n in numbers:
            total += n
        print(total)
c = Calculator()
c.add(10, 20)
c.add(10, 20, 30)
c.add(10, 20, 30, 40)

#Method Overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
a = Animal()
d = Dog()
a.sound()
d.sound()

#Operator Overloading
a = 10
b = 20
print(a + b)