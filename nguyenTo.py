import math
def prime(n):
    if n < 2: return False
    else:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0: return False
    return True
for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(1, n):
        if math.gcd(n, i) == 1: count += 1
    if prime(count): print("YES")
    else: print("NO")