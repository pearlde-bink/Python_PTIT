import math
for t in range(int(input())):
    n, x, m = [float(i) for i in input().split()]
    x /= 100
    year = math.ceil(math.log((m / n), (1 + x)))
    print(year)