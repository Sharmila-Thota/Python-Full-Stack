#Functions
#add two Variables
def Add(a,b):
    print(a+b)
print(10,20)
print(30,20)
print(50,33)

#positional Arguments
#calling function with arguments with return type
def Add(a,b):
    c=a+b
    return c
r=Add(10,20)
print(r)

#calling function with argument without return type
print("start-1")
def Add(a,b):
    c=a+b
    print("start-3")
    return c
    print("end - 1")
print("start-2")
result=Add(10,20)
print(result)
print("end of end")

#calling function without argument with return type:
def Greet():
    return "welcome to hyd"
r=Greet()
print(r)

#calling function without argument without return type:
print("hello")

#keyword Arguments
def Greet(name, age):
    print(f"my name is {name} and age is {age}")
Greet(name="Raju", age=23)
Greet(age = 24, name="harisha")

#Default parameter
def country_details(country="india"):
    print("my country name is :" , country)
country_details("usa")
country_details()

#orbitary arguments 
def Itembill(*l):
    print(l)
    print(l[0])
Itembill(10,20,30,40,50,60,70,80)

#keyword orbitary arguments
def user_info(**details):
    print(details)
    print(details['name'])
user_info(name="raju",age=23,height=5.7)

