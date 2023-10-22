import math
def prime(n):
    if n < 2: return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0: return False
    return True

n = int(input())
a = [int(x) for x in input().split()]
di = {}

for i in a:
    if prime(i):
        if i in di:
            di[i] += 1
        else: di[i] = 1    
for i in di:
    print(i, di[i])
            
