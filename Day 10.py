# String Built-in Methods

s = "sharmila"

# 1. capitalize()
print("capitalize:", s.capitalize())

# 2. title()
print("title:", s.title())

# 3. istitle()
print("istitle:", s.istitle())

# 4. lower()
print("lower:", s.lower())

# 5. upper()
print("upper:", s.upper())

# 6. swapcase()
print("swapcase:", s.swapcase())

# 7. startswith()
print("startswith:", s.startswith("s"))

# 8. endswith()
print("endswith:", s.endswith("a"))

# 9. strip()
s1 = "  sharmila  "
print("strip:", s1.strip())

# 10. rstrip()
print("rstrip:", s1.rstrip())

# 11. count()
print("count:", s.count("a"))

# 12. index()
print("index:", s.index("s"))

# 13. rindex()
print("rindex:", s.rindex("a"))

# 14. find()
print("find:", s.find("s"))

# 15. rfind()
print("rfind:", s.rfind("r"))

# 16. isidentifier()
print("isidentifier:", s.isidentifier())

# 17. split()
h = "hello world"
print("split:", h.split())

# 18. join()
l = ["apple", "orange", "banana"]
print("join:", " ".join(l))

# 19. center()
print("center:", s.center(20))

# 20. encode()
data = s.encode()
print("encode:", data)

# 21. decode()
print("decode:", data.decode())