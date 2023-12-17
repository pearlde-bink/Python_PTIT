s = input()
b = {}
if len(s) % 2 != 0: s = s[:-1]
i = 0
while i < len(s) - 1:
    a = str(s[i]) + str(s[i+1])
    if b.get(a) == None:
        b.update({a:1})
    else: b.update({a:b.get(a)+1})
    i += 2
for x, y in b.items():
    print(x, y, sep = " ")