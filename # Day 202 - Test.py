# Day 202 - Test

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


tests = [
    (
        [[1, 3], [2, 6], [8, 10], [9, 12]],
        [[1, 6], [8, 12]],
    ),
    (
        [[1, 4], [4, 5]],
        [[1, 5]],
    ),
    (
        [[5, 7], [1, 2], [3, 4]],
        [[1, 2], [3, 4], [5, 7]],
    ),
    ([], []),
]

for intervals, expected in tests:
    assert merge_intervals(intervals) == expected

print("Day 202 test ok")