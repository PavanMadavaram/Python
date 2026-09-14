# Day 198 - Search Helper

def hours_needed(piles, speed):
    return sum((pile + speed - 1) // speed for pile in piles)


def min_eating_speed(piles, hours):
    left = 1
    right = max(piles)

    while left < right:
        speed = (left + right) // 2

        if hours_needed(piles, speed) <= hours:
            right = speed
        else:
            left = speed + 1

    return left


piles = [30, 11, 23, 4, 20]
hours = 6

print("Minimum speed:", min_eating_speed(piles, hours))