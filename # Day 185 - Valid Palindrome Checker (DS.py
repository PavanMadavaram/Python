# Day 185 - Valid Palindrome Checker (DSA: Two Pointers)

def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


samples = [
    "A man, a plan, a canal: Panama",
    "race a car",
    "Was it a car or a cat I saw?",
    "hello world",
]

print("🔍 Valid Palindrome Analysis (Two-Pointer Method):\n")
for phrase in samples:
    verdict = "✅ Palindrome" if is_palindrome(phrase) else "❌ Not palindrome"
    print(f"• \"{phrase}\" -> {verdict}")