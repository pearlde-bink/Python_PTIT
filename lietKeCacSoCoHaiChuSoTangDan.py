s = input()
b = {}
if len(s) % 2 != 0: s = s[:-1]
i = 0
while i < len(s) - 1:
    a = str(s[i]) + str(s[i+1])
    b[a] = 1
    i += 2
c = list(b.keys())
c.sort()
print(*c)