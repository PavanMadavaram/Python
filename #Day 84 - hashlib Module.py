#Day 84 - hashlib Module 
import hashlib

# MD5 hash
text = "Hello Python Day 84"
md5_hash = hashlib.md5(text.encode()).hexdigest()
print("MD5:", md5_hash)

# SHA256
sha256_hash = hashlib.sha256(text.encode()).hexdigest()
print("SHA256:", sha256_hash[:16], "...")