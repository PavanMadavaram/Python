# Day 183 - Test

def get_active_topics(topic_list):
    return [t["topic"] for t in topic_list if t["status"] == "in progress"]


sample = [
    {"topic": "Arrays", "status": "completed"},
    {"topic": "Trees", "status": "in progress"},
    {"topic": "Graphs", "status": "in progress"},
]

print("Day 183 test:", len(get_active_topics(sample)) == 2)
print("Day 183 test ok")