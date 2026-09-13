# Day 197 - Test

def find_minimum(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        middle = (left + right) // 2

        if numbers[middle] > numbers[right]:
            left = middle + 1
        else:
            right = middle

    return numbers[left]


tests = [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([11, 13, 15, 17], 11),
    ([2, 1], 1),
    ([1], 1),
]

for numbers, expected in tests:
    assert find_minimum(numbers) == expected

print("Day 197 test ok")