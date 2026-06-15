#Day 112 - Test
import heapq

data = [4, 1, 3]
heapq.heapify(data)
print("Heap test:", heapq.heappop(data) == 1)
print("Day 112 test ok")