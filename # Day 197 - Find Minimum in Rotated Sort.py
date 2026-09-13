# Day 197 - Find Minimum in Rotated Sorted Array
# DSA: Modified Binary Search

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


arrays = [
    [3, 4, 5, 1, 2],
    [4, 5, 6, 7, 0, 1, 2],
    [11, 13, 15, 17],
]

for numbers in arrays:
    print(f"{numbers} -> minimum: {find_minimum(numbers)}")