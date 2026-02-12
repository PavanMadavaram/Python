# Day 9 Helper Functions
def double_numbers(numbers):
    """Double every number in list"""
    result = []
    for num in numbers:
        result.append(num * 2)
    return result

def filter_evens(numbers):
    """Return only even numbers"""
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

def print_with_index(items):
    """Print with numbers"""
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

# Demo
data = [5, 12, 8, 15, 20]
print("Doubled:", double_numbers(data))
print("Evens:", filter_evens(data))
print_with_index(["Python", "SQL", "Git"])
