import string

def is_palindrome(text: str) -> bool:
    allowed = string.ascii_letters + string.digits
    cleaned = "".join(ch.lower() for ch in text if ch in allowed)
    return cleaned == cleaned[::-1]

print(is_palindrome("Kasur ini rusak"))   # True
print(is_palindrome("Hello World"))       # False
