# Day 8 - Dictionaries (Key-Value Pairs)
profile = {
    "name": "Raju Kumar",
    "age": 22,
    "city": "Hyderabad",
    "job": "Python Developer",
    "skills": ["Python", "SQL", "GitHub"]
}

print("👤 Profile:", profile)
print("📛 Name:", profile["name"])
print("🏙️  City:", profile["city"])
print("💼 Skills:", profile["skills"])
print("🔑 All keys:", list(profile.keys()))
print("📊 Length:", len(profile))

print("✅ Day 8 Complete!")
