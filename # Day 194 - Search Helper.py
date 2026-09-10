# Day 194 - Search Helper

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


values = [1, 3, 5, 7, 9, 11]

print("Index of 7:", binary_search(values, 7))
print("Index of 8:", binary_search(values, 8))