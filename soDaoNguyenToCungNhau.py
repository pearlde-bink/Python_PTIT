import math
for _ in range(int(input())):
    n = int(input())
    s1 = str(n)
    s = int(s1[::-1])
    if math.gcd(s, n) == 1: print("YES")
    else: print("NO")
    