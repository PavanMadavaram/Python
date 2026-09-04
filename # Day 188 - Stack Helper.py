# Day 188 - Stack Helper

def next_greater_element(nums):
    result = [-1] * len(nums)
    stack = []

    for index, value in enumerate(nums):
        while stack and value > nums[stack[-1]]:
            previous_index = stack.pop()
            result[previous_index] = value

        stack.append(index)

    return result


sample = [13, 7, 6, 12]
print("Result:", next_greater_element(sample))