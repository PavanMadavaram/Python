# Day 190 - Sliding Window Maximum
# DSA: Monotonic Deque

from collections import deque

def max_sliding_window(nums, k):
    result = []
    dq = deque()  # Stores indices of potential maximums

    for i, value in enumerate(nums):
        # Remove indices outside the current window
        if dq and dq[0] == i - k:
            dq.popleft()

        # Maintain decreasing order in deque
        while dq and nums[dq[-1]] <= value:
            dq.pop()

        dq.append(i)

        # Append maximum once the first full window is formed
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


numbers = [1, 3, -1, -3, 5, 3, 6, 7]
window_size = 3
answer = max_sliding_window(numbers, window_size)

print("Numbers:       ", numbers)
print(f"Window size:   {window_size}")
print("Max in window: ", answer)