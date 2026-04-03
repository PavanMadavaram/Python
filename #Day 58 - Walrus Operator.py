#Day 58 - Walrus Operator 
# Assign AND use in same expression

# Old way
numbers = [1, 2, 3, 4]
if (n := len(numbers)) > 3:
    print(f"List has {n} items")

# Inline assignment
while (line := input("Enter text: ")) != "quit":
    print("You entered:", line)
