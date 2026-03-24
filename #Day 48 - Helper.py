#Day 48 - Helper
def has_even(numbers):
    return any(n % 2 == 0 for n in numbers)

print("Has even?", has_even([1, 3, 4, 5]))
