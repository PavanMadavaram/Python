# Day 194 - Binary Search
# DSA: Search in a sorted array

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


numbers = [2, 4, 7, 11, 15, 19, 24]
target = 15

index = binary_search(numbers, target)

print("Numbers:", numbers)
print("Target:", target)
print("Index:", index)