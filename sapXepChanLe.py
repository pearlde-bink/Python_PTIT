n = int(input())
a = []
while len(a) < n:
    a += [int(i) for i in input().split()]
m = [0]*len(a)
chan, le = [], []
for i in range(len(a)):
    if a[i] % 2:
        le += [a[i]]
    else:
        m[i] = 1
        chan += [a[i]]
chan.sort()
le.sort(key = lambda k: -k)
i, j = 0, 0
for k in range(n):
    if m[k]:
        print(chan[i], end = " ")
        i += 1
    else:
        print(le[j], end = " ")
        j += 1