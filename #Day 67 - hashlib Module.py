#Day 67 - hashlib Module 
import hashlib

password = "mypassword123"
hash_object = hashlib.sha256(password.encode())
print("Password hash:", hash_object.hexdigest())