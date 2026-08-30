# Day 184 - Test

def find_two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None


nums = [3, 2, 4]
target = 6
indices = find_two_sum(nums, target)

print("Day 184 test:", indices == (1, 2))
print("Day 184 test ok")