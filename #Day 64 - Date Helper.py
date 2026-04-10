#Day 64 - Date Helper
from datetime import datetime, timedelta

yesterday = datetime.now() - timedelta(days=1)
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
