#Day 84 - Test
import hashlib
test_hash = hashlib.md5(b'test').hexdigest()
print("Hash test:", test_hash == '098f6bcd4621d373cade4e832627b4f6')
print("Day 84 test ok")