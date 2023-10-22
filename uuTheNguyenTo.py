import math
def prime(n):
    if n < 2: return False
    else:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0: return False
    return True

for _ in range(int(input())):
    dem = 0
    n = input()
    for i in n:
        if prime(int(i)): dem += 1
    if dem > len(n) - dem and prime(len(n)): print("YES")
    else: print("NO")