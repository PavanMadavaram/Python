# Day 203 - Non-Overlapping Intervals
# DSA: Sorting + Greedy

def erase_overlap_intervals(intervals):
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda interval: interval[1])
    kept = 1
    previous_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= previous_end:
            kept += 1
            previous_end = end

    return len(intervals) - kept


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]

print("Intervals:", intervals)
print("Minimum removals:", erase_overlap_intervals(intervals))