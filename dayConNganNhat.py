from math import gcd
for _ in range(int(input())):
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a += [-1]
    dem, val = 0, 1000000
    for i in range(len(a)-1):
        if a[i] % k == 0:   
            if a[i] == k:
                dem += 1
            else:
                if gcd(a[i], a[i+1]) == k:
                    dem += 2
            if dem != 0: 
                val = min(val, dem)
        else: dem = 0
            
    print(val if val != 1000000 and val != 0 else -1) 
