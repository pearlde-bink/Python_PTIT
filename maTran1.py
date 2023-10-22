n = int(input())
a = []
for i in range (n):
    b = list(map(int, input().split()))
    a.append(b)
  
s1 = s2 = 0
for i in range(0, n):
    for j in range(0, n):
        if i < j: s1 += a[i][j]
        elif i > j: s2 += a[i][j]
        
k = int(input())
if abs(s2 - s1) <= k: print("YES")
else: print("NO")
print(abs(s2 - s1))

    