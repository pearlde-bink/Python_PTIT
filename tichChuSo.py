def tich(n):
    t = 1
    while n > 0:
        d = n % 10
        if d: t *= d
        n //= 10
    return t
for _ in range(int(input())):
    n = int(input())
    print(tich(n))
