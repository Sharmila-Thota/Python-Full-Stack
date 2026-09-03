#List
l = [1, 2, 3, 4, 5]
#Operations on List
#concatenation
l1 = [6, 7, 8]
l2 = [9, 10, 11]
l3 = l1 + l2
print("Concatenation:", l3)
#repetition
l4 = l1 * 2
print("Repetition:", l4)    
#Indexing
print("Indexing:", l[0])
#slicing
print("Slicing:", l[1:4])
#membership
print("Membership:", 3 in l)
print("Membership:", 6 not in l)
#Functions on List
print("minimum:", min(l))
print("maximum:", max(l))
print("length:", len(l))
print("sorting:", sorted(l))
print("sum:", sum(l))
#Methods on List
#append()
l.append(6)
print("append:", l)
#extend()
l.extend([7, 8])
print("extend:", l)
#insert()
l.insert(2, 9)
print("insert:", l)
#remove()
l.remove(4)
print("remove:", l)
#clear()
l.clear()
print("clear:", l)
#pop()  
l = [1, 2, 3, 4, 5]
popped_element = l.pop()
print("pop:", popped_element)
#delete()
del l[0]
print("delete:", l)
#count()
l = [1, 2, 3, 2, 4, 2]
print("count:", l.count(2))
#index()
print("index:", l.index(3))
#Nested List
l = [[1, 2], [3, 4], [5, 6]]
print(l[0][1])  
print("Nested List:", l)
#Tuple
t1 = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)
#operations on tuple
#concatenation
t3 = t1 + t2
print("Concatenation:", t3)
#repetition
print("Repetition:", t1 * 2)
#indexing
print("Indexing:", t1[0])
#slicing
print("Slicing:", t1[1:4])
#membership
print("Membership:", 3 in t1)
print("Membership:", 6 not in t1)
# Functions 
#minimum()
print("minimum:", min(t1))
#maximum()
print(max(t1))
#length()
print("length:", len(t1))
#sorted()
print("sorting:", sorted(t1))
#sum()
print("sum:", sum(t1))
#tuple()
print(t1)
#any()
print("any:", any(t1))
#all()
print("all:", all(t1))




