# Set
id1 = {1, 2, 3, 4, 5}
id2 = {6, 5, 8, 9, 10}
print("Set:", id1)

# Operations on set

# Membership
print("Membership:", 3 in id1)

# Union
print("Union:", id1 | id2)

# Intersection
print("Intersection:", id1 & id2)

# Difference
print("Difference:", id1 - id2)

# Symmetric Difference
print("Symmetric Difference:", id1 ^ id2)


# Methods

# add()
id1.add(12)
print("After add:", id1)

# update()
id2.update([1, 40])
print("After update:", id2)

# discard()
id1.discard(1)
print("After discard:", id1)

# pop()
id4 = {24, 56, 7, 8}
print("Popped element:", id4.pop())
print("After pop:", id4)


# union()
print("Union:", id1.union(id2))

# intersection()
print("Intersection:", id1.intersection(id2))

# difference()
print("Difference:", id1.difference(id2))

# symmetric_difference()
print("Symmetric Difference:", id1.symmetric_difference(id2))

# issubset()
print("Is subset:", id1.issubset(id2))

# isdisjoint()
print("Is disjoint:", id1.isdisjoint(id2))

# issuperset()
print("Is superset:", id1.issuperset(id2))


# Dictionary

student = {
    "name": "Sharmila",
    "age": 22,
    "course": "Python"
}

student2 = {
    "city": "Vijayawada",
    "age": 23,
    "language": "English"
}

print("Dictionary:", student)

# Operations on Dictionary

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Membership
print("Membership:", "name" in student)

# Adding new key-value pair
student["city"] = "Vijayawada"
print("After adding:", student)

# Updating value
student["age"] = 23
print("After updating:", student)

# Functions

# len()
print("Length:", len(student))

# type()
print("Type:", type(student))

# Methods

# get()
print("Get:", student.get("name"))

# keys()
print("Keys:", student.keys())

# values()
print("Values:", student.values())

# items()
print("Items:", student.items())

# update()
student.update({"phone": 9876543210})
print("After update:", student)

# pop()
student.pop("phone")
print("After pop:", student)


# popitem()
student.popitem()
print("After popitem:", student)

# setdefault()
student.setdefault("country", "India")
print("After setdefault:", student)

# copy()
copied_student = student.copy()
print("Copied Dictionary:", copied_student)

# clear()
copied_student.clear()
print("After clear:", copied_student)

# delete
del copied_student

# Merging dictionaries
merged_student = {**student, **student2}
print("Merged Dictionary:", merged_student)

# Nested Dictionary
students = {
    "student1": {
        "name": "Sharmila",
        "age": 22,
        "course": "Python"
    },

    "student2": {
        "name": "Ravi",
        "age": 23,
        "course": "Java"
    }
}
print("Nested Dictionary:", students)

# Accessing nested dictionary
print("Student 1 Name:", students["student1"]["name"])
print("Student 2 Course:", students["student2"]["course"])

# Updating nested dictionary
students["student1"]["age"] = 23
print("After updating nested:", students)

# Adding to nested dictionary
students["student1"]["city"] = "Vijayawada"
print("After adding to nested:", students)

# Nested Dictionary using loop
for student_name, details in students.items():
    print(student_name)
    print(details)