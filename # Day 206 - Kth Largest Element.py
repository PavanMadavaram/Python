# Day 206 - Kth Largest Element
# DSA: Min-Heap

import heapq


def kth_largest(numbers, k):
    heap = []

    for number in numbers:
        heapq.heappush(heap, number)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


numbers = [3, 2, 1, 5, 6, 4]
k = 2

print("Numbers:", numbers)
print(f"{k}th largest:", kth_largest(numbers, k))