#Regular Expression
#re.search()
import re

text = "I am learning Python"

result = re.search("Python", text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")

#re.match()
import re

text = "Python is easy"

result = re.match("Python", text)

if result:
    print("Matched")
else:
    print("Not matched")

#re.findall()
import re

text = "apple banana apple mango apple"

result = re.findall("apple", text)

print(result)


import re

phone = input("Enter phone number: ")

if re.fullmatch(r"\d{10}", phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

#Check email
import re

email = input("Enter email: ")

pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

if re.fullmatch(pattern, email):
    print("Valid email")
else:
    print("Invalid email")

#