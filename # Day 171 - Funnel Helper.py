# Day 171 - Funnel Helper

events = ["visit", "signup", "login", "purchase"]
target = "login"

print("Reached target:", target in events)
print("Progress:", f"{(events.index(target) + 1) / len(events):.0%}")