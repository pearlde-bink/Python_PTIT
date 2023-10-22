import math
def prime(n):
    if n < 2: return False
    else:
        for i in range (2, int(math.sqrt(n) + 1)):
            if n % i == 0: return False
    return True

def isValid(n):
    s = str(n)
    for i in range(0, len(s), 2):
        if int(s[i]) % 2 != 0: return False
        
    for i in range(1, len(s), 2):
        if int(s[i]) % 2 == 0: return False
        
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    if not prime(sum): return False
    
    return True
    
for _ in range(int(input())):
    n = int(input())
    print("YES" if isValid(n) else "NO")
