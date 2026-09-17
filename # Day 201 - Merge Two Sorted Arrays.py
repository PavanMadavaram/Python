# Day 201 - Merge Two Sorted Arrays
# DSA: Two Pointers

def merge_sorted_arrays(first, second):
    result = []
    left = 0
    right = 0

    while left < len(first) and right < len(second):
        if first[left] <= second[right]:
            result.append(first[left])
            left += 1
        else:
            result.append(second[right])
            right += 1

    result.extend(first[left:])
    result.extend(second[right:])

    return result


first = [1, 4, 7, 10]
second = [2, 3, 8, 11]

print("First array: ", first)
print("Second array:", second)
print("Merged:      ", merge_sorted_arrays(first, second))