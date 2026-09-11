# Day 195 - Search Insert Position
# DSA: Binary Search

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


numbers = [1, 3, 5, 6]
targets = [5, 2, 7, 0]

for target in targets:
    position = search_insert(numbers, target)
    print(f"Target {target}: insert at index {position}")