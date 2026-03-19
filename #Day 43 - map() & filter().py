#Day 43 - map() & filter() 
numbers = [1, 2, 3, 4, 5]

# Double all numbers
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)

# Only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)
