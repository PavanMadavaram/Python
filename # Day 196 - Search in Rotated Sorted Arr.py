# Day 196 - Search in Rotated Sorted Array
# DSA: Modified Binary Search

def search_rotated(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        # Left half is sorted
        if numbers[left] <= numbers[middle]:
            if numbers[left] <= target < numbers[middle]:
                right = middle - 1
            else:
                left = middle + 1

        # Right half is sorted
        else:
            if numbers[middle] < target <= numbers[right]:
                left = middle + 1
            else:
                right = middle - 1

    return -1


numbers = [4, 5, 6, 7, 0, 1, 2]
target = 0

print("Numbers:", numbers)
print("Target:", target)
print("Index:", search_rotated(numbers, target))