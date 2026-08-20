# Day 174 - Habit Helper

def calculate_streak(days):
    streak = 0

    for completed in days:
        if completed:
            streak += 1
        else:
            streak = 0

    return streak


progress = [True, True, True, True]

print("Current streak:", calculate_streak(progress))