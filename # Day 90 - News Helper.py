# Day 90 - News Helper
import json
from pathlib import Path

sample = {
    "source": "local",
    "articles": [
        {"title": "Python Roadmap Complete", "body": "Built 90 days of Python practice."}
    ]
}

Path("news_backup.json").write_text(json.dumps(sample, indent=4))
print("Backup saved to news_backup.json")