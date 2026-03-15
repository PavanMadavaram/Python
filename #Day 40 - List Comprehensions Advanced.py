#Day 40 - List Comprehensions Advanced 
numbers = [1, 2, 3, 4, 5, 6]

# Even only
evens = [x for x in numbers if x % 2 == 0]
print("Evens:", evens)

# Squared
squares = [x**2 for x in numbers]
print("Squares:", squares)
