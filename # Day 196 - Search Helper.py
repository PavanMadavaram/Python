# Day 196 - Search Helper

def search_rotated(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        if numbers[left] <= numbers[middle]:
            if numbers[left] <= target < numbers[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if numbers[middle] < target <= numbers[right]:
                left = middle + 1
            else:
                right = middle - 1

    return -1


values = [6, 7, 8, 1, 2, 3, 4, 5]

print("Index of 3:", search_rotated(values, 3))
print("Index of 9:", search_rotated(values, 9))