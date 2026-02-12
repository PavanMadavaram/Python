# Day 9 - Looping Through Lists
numbers = [10, 20, 30, 40, 50]
print("📊 Original numbers:", numbers)

# Task 1: Double each number
doubled = []
for num in numbers:
    doubled.append(num * 2)
print("🔢 Doubled:", doubled)

# Task 2: Find even numbers only
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print("➖ Even numbers:", evens)

print("✅ Day 9 Complete!")
