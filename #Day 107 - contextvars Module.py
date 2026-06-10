#Day 107 - contextvars Module 
import contextvars

user = contextvars.ContextVar("user", default="guest")

print("Default user:", user.get())

token = user.set("admin")
print("Updated user:", user.get())

user.reset(token)
print("Reset user:", user.get())