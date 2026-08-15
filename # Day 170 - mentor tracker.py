# Day 170 - mentor tracker

mentors = [
    {"name": "Python documentation", "lesson": "Read official examples"},
    {"name": "Practice project", "lesson": "Learn by building"},
    {"name": "Code review", "lesson": "Improve through feedback"},
]

for mentor in mentors:
    print(f"{mentor['name']}: {mentor['lesson']}")