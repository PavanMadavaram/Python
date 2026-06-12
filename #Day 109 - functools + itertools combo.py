#Day 109 - functools + itertools combo
from functools import reduce
import itertools

nums = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, nums)
pairs = list(itertools.combinations(nums, 2))

print("Product:", product)
print("Pairs:", pairs[:5])