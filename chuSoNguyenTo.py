import math
def prime(n):
    if n < 2: return False
    else:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0: return False
    return True

def isValid(n):
    if not prime(len(n)): return False
    dem = 0
    for i in n:
        if prime(int(i)): dem += 1
    if len(n) - dem > dem: return False
    return True

for _ in range(int(input())):
    n = input()
    if isValid(n): print("YES")
    else: print("NO")