#Reverse number
n = int(input("Enter a number:"))
rev = 0
while n > 0:
    r = n % 10
    rev=rev * 10 + r
    n = n // 10
print("Reverse number is :",rev)

#Palindrome number
n = int(input("Enter a number:"))
original = n
rev = 0
while n > 0:
    r = n % 10
    rev=rev * 10 + r
    n = n // 10
if original == rev:
    print("Palindrome")
else:
    print("not palindrome")

#factors of a number
n=6
for i in range(1,n+1):
    if n % i == 0:
        print(i)

#count of factors
n=4
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print(count)

#prime number
n=int(input("enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")

#factorial
n=5
fact=1
for i in range(1,n+1):
    fact = fact * i
print(fact)

#reverse the  list
l =[1,2,3,4,5]
print(l[::-1])

