#Number Patterns
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

print("hello")

r=4
for i in range(1,r+1):
    for j in range(i):
        print(j,end=" ")
    print()

print("hello")

r=4
for i in range(1,r+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("hello")

r=3
c=1
for i in range(1,r+1):
    for j in range(i):
        print(c,end=" ")
        c=c+1
    print()

print("hello")

r=3
c=65
for i in range(1,r+1):
    for j in range(i):
        print(chr(c),end=" ")
        c=c+1
    print()

print("hello")

#HELLOW PATTERNS

r=4
for i in range(r):
    for j in range(r):
        if i==0 or i==r-1 or j==0 or j==r-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")

print("hello")

r=5
for i in range(r):
    for j in range(r):
        if i == r//2 or j==r/2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("hello")

r=5 
for i in range(r):
    for j in range(r):
        if i==j or i+j==r-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()