# Day 188 - Test

def next_greater_element(nums):
    result = [-1] * len(nums)
    stack = []

    for index, value in enumerate(nums):
        while stack and value > nums[stack[-1]]:
            previous_index = stack.pop()
            result[previous_index] = value

        stack.append(index)

    return result


tests = [
    ([4, 5, 2, 10, 8], [5, 10, 10, -1, -1]),
    ([13, 7, 6, 12], [ -1, 12, 12, -1]),
    ([9, 8, 7, 6], [-1, -1, -1, -1]),
    ([1, 2, 3, 4], [2, 3, 4, -1]),
]

for nums, expected in tests:
    assert next_greater_element(nums) == expected

print("Day 188 test ok")