#Day 47 - args Helper
def average(*numbers):
    return sum(numbers) / len(numbers)

print("Average:", average(10, 20, 30))
