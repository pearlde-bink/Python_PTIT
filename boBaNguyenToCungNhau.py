import math
l, r = map(int, input().split())
for i in range(l, r - 1):
    for j in range(i + 1, r):
        for k in range(j + 1, r + 1):
            if math.gcd(k, i) == 1 and math.gcd(k, j) == 1 and math.gcd(i, j) == 1:
                print("(", i, ", ", j, ", ", k, ")", sep = "")
