n = int(input())
a = [[0]] * n
t, d = 0, 0
for i in range(n):
    a[i] = [int(i) for i in input().split()]
for i in range(n):
    for j in range(n):
        if j > i: t += a[i][j]
        elif i > j: d += a[i][j]
k = int(input())
if t - d <= k: 
    print("YES")
else:
    print("NO")
print(abs(t-d))
'''
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
'''
