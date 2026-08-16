# Day 171 - funnel tracker

sessions = {
    "user_001": ["visit", "signup", "login", "purchase"],
    "user_002": ["visit", "signup"],
    "user_003": ["visit", "signup", "login"],
}

steps = ["visit", "signup", "login", "purchase"]

for step in steps:
    count = sum(step in events for events in sessions.values())
    print(f"{step}: {count}")