def compress(s: str) -> str:
    if not s:
        return s
    res_parts = []
    prev = s[0]
    count = 1
    for ch in s[1:]:
        if ch == prev:
            count += 1
        else:
            res_parts.append(f"{prev}{count}")
            prev = ch
            count = 1
    res_parts.append(f"{prev}{count}")
    encoded = "".join(res_parts)
    return encoded if len(encoded) <= len(s) else s

print(compress("aaabbc"))  # a3b2c1
print(compress("abcd"))    # abcd
print(compress("aaaa"))    # a4
