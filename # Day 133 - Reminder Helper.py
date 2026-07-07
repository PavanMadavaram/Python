# Day 133 - Reminder Helper
from datetime import datetime, timedelta

due = datetime.now() + timedelta(minutes=30)
print(due.strftime("%H:%M"))