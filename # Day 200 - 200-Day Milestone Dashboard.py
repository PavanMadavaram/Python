# Day 200 - 200-Day Milestone Dashboard

TOTAL_DAYS = 365
CURRENT_DAY = 200

milestones = {
    50: "First milestone",
    100: "100-day streak",
    150: "Halfway to 300",
    200: "200-day milestone",
    250: "Next major milestone",
    300: "Final stretch",
    365: "Year complete",
}

progress = CURRENT_DAY / TOTAL_DAYS * 100
remaining = TOTAL_DAYS - CURRENT_DAY

print("🎉 200-DAY MILESTONE DASHBOARD\n")
print(f"Current day: {CURRENT_DAY}/{TOTAL_DAYS}")
print(f"Progress: {progress:.1f}%")
print(f"Days remaining: {remaining}\n")

print("Milestones:")
for day, name in milestones.items():
    status = "✅ reached" if day <= CURRENT_DAY else "⏳ upcoming"
    print(f"Day {day}: {name} — {status}")