#Patterns
for i in range(4):
    print("*",end =" ")

for i in range(1,5):
    print("*")

for i in range(1,4):
    for j in range(1,4):
        print("*",end =" ")
    print()

for i in range(1,3):
    for j in range(1,5):
        print("*", end=" ")
    print()

for i in range(1,4):
    for j in range(i):
        print("*",end = " ")
    print(i)

r=4
for i in range(1,r+1):
    for k in range(r-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(1,r+1):
    for k in range(r-i):
        print(" ",end=" ")
    for j in range(2 * i-1):
        print("*",end=" ")
    print()

for i in range(r,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(4,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

n=5
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(n-i,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()