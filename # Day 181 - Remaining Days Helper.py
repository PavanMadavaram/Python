# Day 181 - Remaining Days Helper

def calculate_remaining_days(current_day=181, total_days=365):
    return total_days - current_day


days_left = calculate_remaining_days(181)
print(f"Days left to complete the year: {days_left}")