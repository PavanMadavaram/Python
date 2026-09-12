# Day 196 - Test

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


tests = [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([1], 1, 0),
    ([1], 0, -1),
    ([5, 1, 3], 3, 2),
]

for numbers, target, expected in tests:
    assert search_rotated(numbers, target) == expected

print("Day 196 test ok")