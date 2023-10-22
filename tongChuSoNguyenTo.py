import math
def prime(n):
    if n < 2: return False
    else:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0: return False
    return True
for _ in range(int(input())):
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    print("YES" if prime(sum) else "NO")