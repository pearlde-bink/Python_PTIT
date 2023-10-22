import math
def ucln(a, b):
    if b == 0: return a 
    return ucln(b, a % b)
  
def prime(n):
    if n < 2 : return False
    for i in range(2, 1 + math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

for t in range(int(input())):
    li = [int(i) for i in input().split()]
    c = ucln(li[0], li[1])
    sum = 0
    while c > 0:
        sum += c % 10
        c //= 10 
    if prime(sum): print("YES")
    else: print("NO")

