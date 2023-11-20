from math import factorial

n = int(input())
a = []
for i in range(n):
    a.append(list(input()))
cnt = 0
for i in range(n):
    dem2 = 0
    for j in range(n):
        if a[i][j] == "C": dem2 += 1
    if dem2 == 2: cnt += 1
    elif dem2 > 2: cnt += factorial(dem2) // (factorial(2) * factorial(dem2 - 2))

for i in range(n):
    dem2 = 0
    for j in range(n):
        if a[j][i] == "C": dem2 += 1
    if dem2 == 2: cnt += 1
    elif dem2 > 2: cnt += factorial(dem2) // (factorial(2) * factorial(dem2 - 2))
print(cnt)
"""
4
CC..
C..C
.CC.
.CC.
"""
