#Day 87 - Shutil Helper
import shutil
import os

# Make archive of current folder example
base_name = shutil.make_archive('backup_day87', 'zip', '.')
print("Archive created:", base_name)

# Move file example
if os.path.exists('day87_copy.py'):
    shutil.move('day87_copy.py', 'moved_day87_copy.py')
    print("Moved copy file")