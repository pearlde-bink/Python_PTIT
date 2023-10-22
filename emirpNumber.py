# outcome matches result in codeptit but when submitting, it's wrong
'''import math
def prime(n):
    for i in range(2, 1 + math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def reversePrime(n):
    m = reverseNum(n)
    #check if reverse number is prime, not equal to original number and less than n
    return True if (prime(m) and m != n and m < n) else False
#  and reverse < n

def reverseNum(n):
    reverse = 0
    m = n
    while m > 0: 
        reverse = reverse*10 + m%10
        m //= 10
    return reverse

for t in range(int(input())):
    n = int(input())
    li = []
    
    for i in range (13, n):
        if prime(i) and reversePrime(i):
          li.append(reverseNum(i)) 
          li.append(i)
    for i in li:
      print(i, end = " ")
    print() '''
    
from math import sqrt


maxVal = int(1e6+5)
p = [1] * maxVal
p[0] = p[1] = 0
for i in range(2, int(sqrt(maxVal))):
    if p[i]:
        for j in range(i*2, maxVal, i):
            p[j] = 0

for t in range(int(input())):
    n = int(input())
    for i in range(11, n):
        j = int(str(i)[::-1])
        if i < j and j < n and p[i] and p[j]:
            print(i, j, end=' ')
    print()
      
      
