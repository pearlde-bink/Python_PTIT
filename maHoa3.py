def convert(s):
    dem = 0
    val = ''
    for i in s:
        dem += ord(i) - ord('A')
    for i in s:
        val += chr(((ord(i) - ord('A') + dem) % 26 + ord('A')))
    return val

for _ in range(int(input())):
    s = input()
    n = int(len(s) / 2)
    s1 = s[:n]
    s2 = s[n:]
    s1 = convert(s1)
    s2 = convert(s2)
    val = ''
    for i in range(n):
        val += chr(((ord(s1[i]) - 2 * ord('A') + ord (s2[i])) % 26 + ord('A')))
    print(val)