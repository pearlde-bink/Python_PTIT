a, b = [1]*10000, []
for i in range(2, 10000):
    if a[i] == 1:
        for j in range(i*i, 10000, i):
            a[j] = 0
        b.append(i)
n = int(input())
x = [int(i) for i in input().split()]
val = 0
for i in x:
    s = 1000000
    for j in b:
        s = min(s, abs(i-j))
    val = max(val, s)
print(val)
