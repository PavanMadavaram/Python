# Day 198 - Test

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


tests = [
    ([3, 6, 7, 11], 8, 4),
    ([30, 11, 23, 4, 20], 5, 30),
    ([30, 11, 23, 4, 20], 6, 23),
    ([1], 1, 1),
]

for piles, hours, expected in tests:
    assert min_eating_speed(piles, hours) == expected

print("Day 198 test ok")