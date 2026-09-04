#scope
#1.Local Scope
def student():
    name="raju"
    print(name)
student()
print("outside the function:","name")

#Global scope
company="codegnan"
def Display():
    number=100
    print("inside the function:","number")
Display()
print(company)

#non local scope
def outer():
    def inner():
        print("inner")
    inner()
    print("outer")
outer()
print("outer")

#LEGB
print("global scope")
def outer():
    print("enclosing_scope")
    def inner():
        print("local scope")
    inner()
    print("outer")
print("start")

#call by value
def update():
    number=200
number = 100
print("before:",number)
print("after:",number)

#call by reference
def shoppingcart(cart):
    cart.append('orange')
cart=['apple','jam','banana']
print("before:",cart)
shoppingcart(cart)
print("after:",cart)