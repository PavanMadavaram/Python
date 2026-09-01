# Day 185 - Two-Pointer Helper

def clean_alphanumeric(text: str) -> str:
    return "".join(ch.lower() for ch in text if ch.isalnum())


raw_text = "No 'x' in Nixon"
cleaned = clean_alphanumeric(raw_text)

print(f"Original: {raw_text}")
print(f"Cleaned : {cleaned}")
print(f"Reversed: {cleaned[::-1]}")      
