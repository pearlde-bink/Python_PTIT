def tn(s):
    if s == s[::-1]: return True
    return False

f = open("VANBAN.in", "r")
s = 0
b = {}
for x in f:
    t = x.split()
    for i in t:
        if tn(i):
            if len(i) > s:
                s = len(i)
                b.clear()
                b[i] = 1
            elif len(i) == s:
                if not i in b: 
                    b[i] = 1
                else: b[i] += 1
for i in b:
    print(i, b[i])
