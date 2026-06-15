#Day 112 - heapq Module 
import heapq

nums = [7, 2, 9, 1, 5, 3]

heapq.heapify(nums)
print("Min heap:", nums)

heapq.heappush(nums, 0)
print("After push:", nums)

smallest = heapq.heappop(nums)
print("Popped smallest:", smallest)