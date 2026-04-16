#Day 70 - Calendar Helper
import calendar

# Weekday name
print("Monday:", calendar.day_name[0])
print("Day of week (1=Mon):", calendar.MONDAY)

# First weekday of month
print("First weekday April 2026:", calendar.weekday(2026, 4, 1))