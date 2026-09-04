# Day 188 - Next Greater Element
# DSA: Monotonic Stack

def next_greater_element(nums):
    result = [-1] * len(nums)
    stack = []

    for index, value in enumerate(nums):
        while stack and value > nums[stack[-1]]:
            previous_index = stack.pop()
            result[previous_index] = value

        stack.append(index)

    return result


numbers = [4, 5, 2, 10, 8]
answer = next_greater_element(numbers)

print("Input:   ", numbers)
print("Output:  ", answer)