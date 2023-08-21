def repeatedSubstringPattern(s: str) -> bool:
        return s in (s + s)[1:-1]
print(repeatedSubstringPattern("abcabcabcd"))