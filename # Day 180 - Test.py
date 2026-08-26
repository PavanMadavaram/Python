# Day 180 - Test

def calculate_progress(current_day, total_days=365):
    return round((current_day / total_days) * 100, 2)


print("Day 180 test:", calculate_progress(180, 360) == 50.0)
print("Day 180 test ok")