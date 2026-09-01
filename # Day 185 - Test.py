# Day 185 - Test

def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


print("Day 185 test 1:", is_palindrome("Madam, in Eden, I'm Adam") is True)
print("Day 185 test 2:", is_palindrome("Python DSA") is False)
print("Day 185 test ok")