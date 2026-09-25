# Day 209 - Minimum Size Subarray Sum
# DSA: Sliding Window

def min_subarray_length(target, numbers):
    left = 0
    current_sum = 0
    shortest = float("inf")

    for right, value in enumerate(numbers):
        current_sum += value

        while current_sum >= target:
            shortest = min(shortest, right - left + 1)
            current_sum -= numbers[left]
            left += 1

    return 0 if shortest == float("inf") else shortest


numbers = [2, 3, 1, 2, 4, 3]
target = 7

print("Numbers:", numbers)
print("Target:", target)
print("Minimum length:", min_subarray_length(target, numbers))