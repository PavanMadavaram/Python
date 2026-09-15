# Day 199 - Capacity to Ship Packages
# DSA: Binary Search on the Answer

def days_required(weights, capacity):
    days = 1
    current_load = 0

    for weight in weights:
        if current_load + weight > capacity:
            days += 1
            current_load = 0

        current_load += weight

    return days


def minimum_capacity(weights, days):
    left = max(weights)
    right = sum(weights)

    while left < right:
        capacity = (left + right) // 2

        if days_required(weights, capacity) <= days:
            right = capacity
        else:
            left = capacity + 1

    return left


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5

capacity = minimum_capacity(weights, days)

print("Package weights:", weights)
print("Available days:", days)
print("Minimum capacity:", capacity)