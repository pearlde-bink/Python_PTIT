import math
def prime(n):
    if n < 2: return False
    else:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0: return False
    return True

for _ in range(int(input())):
    n = input()
    if prime(int(n[:3])) and prime(int(n[-3:])):
        print("YES")
    else: print("NO")    