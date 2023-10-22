import math
def prime(n):
    if n < 2: 
        return False
    elif n == 2: 
        return True
    else:
        for i in range (3, 1 + math.floor(math.sqrt(n)), 2):
            if n % i == 0: 
                return False
        return True

def sumPrime(n):
    sum = 0
    while n > 0: 
        sum += n%10
        n //= 10
    return True if prime(sum) else False

def eachPrime(n):
    while n > 0:
        if not prime(n%10): return False
        n //= 10
    return True

def reversePrime(n):
    reverse = 0
    while n > 0: 
        reverse = reverse*10 + n%10
        n //= 10
    return True if prime(reverse) else False

for t in range(int(input())):
    n = int(input())
    if prime(n) and sumPrime(n) and eachPrime(n) and reversePrime(n): 
        print("Yes")
    else: print("No")
