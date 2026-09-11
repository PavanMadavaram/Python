# Day 195 - Search Helper

def search_insert(numbers, target):
    left = 0
    right = len(numbers)

    while left < right:
        middle = (left + right) // 2

        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle

    return left


values = [2, 4, 6, 8, 10]

print("Insert position for 6:", search_insert(values, 6))
print("Insert position for 7:", search_insert(values, 7))