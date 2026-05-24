#Day 94 - Traceback Helper
import traceback

def make_error():
    return int("abc")

try:
    make_error()
except Exception:
    err = traceback.format_exc()
    print("Captured error:\n", err)