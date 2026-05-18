#Day 87 - shutil Module
import shutil
import os

# Get disk usage
usage = shutil.disk_usage('.')
print("Total:", usage.total)
print("Used:", usage.used)
print("Free:", usage.free)

# Copy file if it exists
if os.path.exists('day87.py'):
    shutil.copy('day87.py', 'day87_copy.py')
    print("Copied to day87_copy.py")