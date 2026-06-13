#Day 111 - Test
import bisect

nums = [1, 3, 5, 7]
bisect.insort(nums, 4)
print("Bisect test:", nums == [1, 3, 4, 5, 7])
print("Day 111 test ok")