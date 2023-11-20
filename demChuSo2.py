import math

def coun(x, c):
    val = 0
    for i in range(0, 10):
        d = math.pow(10, i)
        if d > c:
            break
        a = c // d
        b = c % d
        z = a % 10
        if z > x: val += ((a // 10) + 1) * d
        elif z == x: val += (a // 10) * d + (b + 1)
        else: val += (a // 10) * d
        if x == 0: val -= d
    return val

def nguyen(x, low, high):
    return coun(x, high) - coun(x, low - 1)

for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(0, 10): print(int(nguyen(i, a, b)), end = ' ')
    print()
    