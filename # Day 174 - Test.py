# Day 174 - Test

def calculate_streak(days):
    streak = 0

    for completed in days:
        if completed:
            streak += 1
        else:
            streak = 0

    return streak


test_days = [True, True, False, True, True]

print("Day 174 test:", calculate_streak(test_days) == 2)
print("Day 174 test ok")