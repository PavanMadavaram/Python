# Day 202 - Interval Helper

def merge_intervals(intervals):
    if not intervals:
        return []

    sorted_intervals = sorted(intervals)
    merged = [sorted_intervals[0][:]]

    for start, end in sorted_intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


calendar = [[5, 7], [1, 3], [2, 4], [9, 11]]

print("Merged calendar:", merge_intervals(calendar))