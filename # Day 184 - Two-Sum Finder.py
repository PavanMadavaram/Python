# Day 184 - Two-Sum Finder 

def find_two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None


numbers = [2, 7, 11, 15]
target_val = 9
result = find_two_sum(numbers, target_val)

print(f"Numbers: {numbers}")
print(f"Target sum: {target_val}")
if result:
    i, j = result
    print(f"Found indices: ({i}, {j}) -> {numbers[i]} + {numbers[j]} = {target_val}")
else:
    print("No pair found.")