# Day 200 - Test

def progress_report(current_day, total_days=365):
    percentage = current_day / total_days * 100
    remaining = total_days - current_day

    return round(percentage, 2), remaining


percentage, remaining = progress_report(200, 400)

assert percentage == 50.0
assert remaining == 200

print("Day 200 test ok")