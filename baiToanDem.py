n = int(input())
a, m, s = [], {}, 0
ok = False
while len(a) < n :
    x = [int(x) for x in input().split()]
    a += x
for i in a :
    m[i] = 1
    s = max(s, i)
for i in range(1, s + 1) :
    if not i in m:
        print(i)
        ok = True
if not ok : print('Excellent!')