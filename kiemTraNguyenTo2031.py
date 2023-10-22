import math
def prime(n):
    if n < 2: return False
    else:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0: return False
    return True

n, m = map(int, input().split())

a = []

for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)

for i in range(0, n):
    for j in range(0, m):
        if prime(a[i][j]):
            a[i][j] = 1
        else: a[i][j] = 0
        print(a[i][j], end = " ")
    print()
