n = int(input())
d = {}
for i in range(n-1):
    a = [int(i) for i in input().split()]
    if not a[1] in d:
        d[a[1]] = 1
    else: d[a[1]] += 1
    if not a[0] in d: 
        d[a[0]] = 1
    else: d[a[0]] += 1
print("Yes" if n - 1 in d.values() else "No")
'''
5
1 2
1 3
1 4
1 5
'''