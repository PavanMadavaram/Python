# Day 194 - Test

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


tests = [
    ([1, 3, 5, 7, 9], 5, 2),
    ([1, 3, 5, 7, 9], 1, 0),
    ([1, 3, 5, 7, 9], 9, 4),
    ([1, 3, 5, 7, 9], 6, -1),
    ([], 4, -1),
]

for numbers, target, expected in tests:
    assert binary_search(numbers, target) == expected

print("Day 194 test ok")