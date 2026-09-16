# Day 200 - Milestone Helper

def progress_report(current_day, total_days=365):
    percentage = current_day / total_days * 100
    remaining = total_days - current_day

    return {
        "percentage": round(percentage, 2),
        "remaining": remaining,
    }


report = progress_report(200)

print("Progress:", f"{report['percentage']:.2f}%")
print("Days remaining:", report["remaining"])