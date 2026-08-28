# Day 181 - Second Half Kickoff Tracker

goals_h2 = [
    {"goal": "Master Object-Oriented Programming", "status": "in progress"},
    {"goal": "Build a full CLI portfolio project", "status": "planned"},
    {"goal": "Automate daily data workflows", "status": "planned"},
    {"goal": "Complete remaining 184 days", "status": "in progress"},
]

print("🚀 Kicking off the second half of the year (Day 181/365)\n")
for item in goals_h2:
    badge = "🔄" if item["status"] == "in progress" else "🎯"
    print(f"{badge} {item['goal']} — [{item['status']}]")