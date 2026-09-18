# Day 202 - Merge Intervals
# DSA: Sorting + Greedy

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals = sorted(intervals)
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        previous_end = merged[-1][1]

        if start <= previous_end:
            merged[-1][1] = max(previous_end, end)
        else:
            merged.append([start, end])

    return merged


intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

print("Original intervals:", intervals)
print("Merged intervals:  ", merge_intervals(intervals))