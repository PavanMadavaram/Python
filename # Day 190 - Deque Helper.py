# Day 190 - Deque Helper

from collections import deque

def max_sliding_window(nums, k):
    result = []
    dq = deque()

    for i, value in enumerate(nums):
        if dq and dq[0] == i - k:
            dq.popleft()

        while dq and nums[dq[-1]] <= value:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


sample = [4, -2, 2, 5, 1]
print("Result:", max_sliding_window(sample, 3))