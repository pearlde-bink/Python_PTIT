s = input()
d = int(input())
a = {}
if len(s) % 2 != 0: s = s[:-1]
i = 0
while i < len(s) - 1:
    k = s[i] + s[i+1]
    if not k in a:
        a[k] = 1
    else:
        a[k] += 1
    i += 2
oke = 0
for i in a.values():
    if i >= d: 
        oke = 1
        break
if oke == 0: print("NOT FOUND")
else:
    b = sorted(a.items(), key = lambda x: x[0])
    for x, y in b:
        if y >= d: print(x, y, sep = " ")
'''
124356141111434356149
2
124356141111434356149
10
'''   
    