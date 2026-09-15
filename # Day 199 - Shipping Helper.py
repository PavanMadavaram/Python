# Day 199 - Shipping Helper

def days_required(weights, capacity):
    days = 1
    current_load = 0

    for weight in weights:
        if current_load + weight > capacity:
            days += 1
            current_load = 0

        current_load += weight

    return days


weights = [3, 2, 2, 4, 1, 4]
capacity = 6

print("Days required:", days_required(weights, capacity))