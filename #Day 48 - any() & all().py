#Day 48 - any() & all() 
numbers = [1, 2, 0, 4]

print("Any > 0?", any(x > 0 for x in numbers))
print("All > 0?", all(x > 0 for x in numbers))

words = ["python", "", "java"]
print("Any truthy?", any(words))
print("All truthy?", all(words))
