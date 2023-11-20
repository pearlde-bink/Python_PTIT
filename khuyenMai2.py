n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = [[]]*n

for i in range(n):
    x[i] = [a[i], b[i]]
x.sort(key=lambda k: k[0]-k[1])

tien = 0
for i in range(k):
    tien = tien + x[i][0]

j = k
while j < n and x[j][0] < x[j][1]:
    tien += x[j][0]
    j+=1
for i in range(j, n): tien += x[i][1]

print(tien)
    

