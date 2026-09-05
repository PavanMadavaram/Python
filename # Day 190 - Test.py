# Day 190 - Test

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


tests = [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
    ([1], 1, [1]),
    ([1, -1], 1, [1, -1]),
    ([9, 11], 2, [11]),
]

for nums, k, expected in tests:
    assert max_sliding_window(nums, k) == expected

print("Day 190 test ok")