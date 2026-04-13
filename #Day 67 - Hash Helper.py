#Day 67 - Hash Helper
import hashlib

data = "Day 67 data"
md5_hash = hashlib.md5(data.encode()).hexdigest()
print("MD5 hash:", md5_hash)