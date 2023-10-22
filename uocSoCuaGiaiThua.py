for _ in range(int(input())):
    n, p = [int(x) for x in input().split()]
    dem = 0
    for i in range (2, n + 1):
        while not i % p:
            i //= p
            dem += 1
    print(dem)