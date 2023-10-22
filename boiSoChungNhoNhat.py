import math

e = 10e9+7
for _ in range(int(input())):
    n, m = map(int, input().split())
    t = n * m
    dem = 2
    for i in range(2, t - 1):
        for j in range(i, t):
            if math.lcm(i, j) == t: dem += 1
            
    print(dem % e)

