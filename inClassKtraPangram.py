import string
def isPangram(s):
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in s.lower(): return False
    return True

str = "The quick brown fox jumps over the lazy dog"
# str = "skjg"
print("YES" if isPangram(str) else "NO")
