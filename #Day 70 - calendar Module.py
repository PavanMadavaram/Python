#Day 70 - calendar Module 
import calendar

# Current month calendar
year, month = 2026, 4
cal = calendar.month(year, month)
print(cal)

# Check leap year
print("2026 leap year?", calendar.isleap(2026))