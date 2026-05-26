#Day 95 - uuid Module 
import uuid

# Generate random UUID
u1 = uuid.uuid4()
print("UUID4:", u1)

# Generate name-based UUID
u2 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
print("UUID5:", u2)