import math

n = int(input())
b = [int(x) for x in input().split()]
b.sort()
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if math.gcd(b[i], b[j]) == 1: print(b[i], b[j], sep = " ")
