import math
n, k = map(int, input().split())
u = 10 ** k
l = 10 ** (k - 1)
count = 0
for i in range(l, u):
    if math.gcd(i, n) == 1: 
        print(i, end = " ")
        count += 1
        if count == 10: 
            print()
            count = 0


