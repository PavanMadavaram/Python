# Day 209 - Sliding Window Helper

def min_subarray_length(target, numbers):
    left = 0
    current_sum = 0
    shortest = len(numbers) + 1

    for right, value in enumerate(numbers):
        current_sum += value

        while current_sum >= target:
            shortest = min(shortest, right - left + 1)
            current_sum -= numbers[left]
            left += 1

    return 0 if shortest == len(numbers) + 1 else shortest


print(min_subarray_length(11, [1, 2, 3, 4, 5]))
print(min_subarray_length(15, [1, 2, 3, 4, 5]))