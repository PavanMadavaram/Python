# Day 197 - Search Helper

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


print("Minimum:", find_minimum([5, 6, 7, 1, 2, 3, 4]))
print("Minimum:", find_minimum([1, 2, 3, 4, 5]))