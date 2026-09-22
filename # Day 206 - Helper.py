# Day 206 - Helper

import heapq


def kth_largest(numbers, k):
    heap = []

    for number in numbers:
        heapq.heappush(heap, number)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


values = [7, 10, 4, 3, 20, 15]

print("2nd largest:", kth_largest(values, 2))
print("4th largest:", kth_largest(values, 4)) 
