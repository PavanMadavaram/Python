#Day 107 - Context Helper
import contextvars

request_id = contextvars.ContextVar("request_id", default=None)

request_id.set("REQ-107")
print("Request ID:", request_id.get())