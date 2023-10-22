import math
a = [2]
def prime(n):
    if n < 2: return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0: return False
    return True

for i in range(3, 1000):
    if prime(i): a.append(i)

n, x = map(int, input().strip().split())
b = [x]
for i in range(1, n+1):
    b.append(b[i-1] + a[i-1])

print(*b)
