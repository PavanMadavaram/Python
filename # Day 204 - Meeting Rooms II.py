# Day 204 - Meeting Rooms II
# DSA: Sorting + Min-Heap

import heapq


def minimum_rooms(intervals):
    if not intervals:
        return 0

    intervals = sorted(intervals)
    end_times = []

    for start, end in intervals:
        if end_times and end_times[0] <= start:
            heapq.heappop(end_times)

        heapq.heappush(end_times, end)

    return len(end_times)


meetings = [[0, 30], [5, 10], [15, 20]]

print("Meetings:", meetings)
print("Minimum rooms required:", minimum_rooms(meetings))