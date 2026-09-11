# Day 195 - Test

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


tests = [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
    ([], 10, 0),
]

for numbers, target, expected in tests:
    assert search_insert(numbers, target) == expected

print("Day 195 test ok")