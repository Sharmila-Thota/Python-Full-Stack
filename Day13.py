#Conditional statements

#if
a = 10
if a > 5:
    print("Hello")

#if - else
num = 16
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#elif
a=19
b=20
c=50
if a>b and a>c:
    print("a is largest")
elif b > a and b > c:
    print("b is largest")
else:
    print("c is largest")

#Nested if
age =20
weight = 53
if age >=18:
    if weight >= 50:
        print("eligible")
    else:
        print(" not eligible")
else:
    print("not eligible")

#Loops

#for loop
l=[1,2,3,4,5]
for i in l:
    print(i)

#Jumping statements
for i in range(1,6,1):
    if i == 4:
        break
    print(i)

#continue

for i in range(1,6,1):
    if i == 4:
        continue
    print(i)



