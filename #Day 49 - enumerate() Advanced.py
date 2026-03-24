#Day 49 - enumerate() Advanced 
fruits = ["apple", "banana", "cherry"]

# With start
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# Get index of item
idx = next(i for i, f in enumerate(fruits) if f == "banana")
print("Banana index:", idx)
