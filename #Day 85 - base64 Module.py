#Day 85 - base64 Module 
import base64

# Encode text
text = "Hello Python Day 85"
encoded = base64.b64encode(text.encode())
print("Encoded:", encoded.decode())

# Decode text
decoded = base64.b64decode(encoded).decode()
print("Decoded:", decoded)