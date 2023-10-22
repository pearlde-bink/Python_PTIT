import math
def prime(n):
    if n < 2: return False
    else:
        for i in range(2, math.floor(math.sqrt(n) + 1)):
            if n % i == 0: return False
    return True

for _ in range(int(input())):
    n = input()
    check = False
    for i in range(0, len(n)):
        if prime(i):
            if prime(int(n[i])): 
                check = True
            else: 
                check = False
                break
        if not prime(i):
            if prime(int(n[i])): 
                check = False
                break
            else: 
                check = True
    print("YES" if check else "NO")
