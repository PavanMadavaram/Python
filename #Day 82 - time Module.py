#Day 82 - time Module 

import time

# Current time
print("Current time:", time.ctime())

# Sleep
print("Sleeping 2 seconds...")
time.sleep(2)
print("Awake!")

# Time components
t = time.localtime()
print("Hour:", t.tm_hour, "Minute:", t.tm_min)