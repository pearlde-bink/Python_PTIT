import math
def biSearch(a, n):
    left = 0
    right = len(a) - 1
    mid = 0
    while left < right:
        mid = (left + right) // 2 
        if a[mid] > n:
            left = mid + 1
        elif a[(left + right) / 2] < n:
            right = mid - 1
        else: return mid
    return -1
def prime(n):
    if n < 2: return 0
    else:
        for i in range(2, math.sqrt(n) + 1):
            if n % i == 0: return 0
    return 1

pr = [1000]
for i in range (1000):
    if prime(i): pr[i] = i
    else: pr[i] = 0
            
n = int(input())
a = [int(i) for i in input().split()]
cnt = 0
for i in range(len(a)):
    if prime(a[i]): cnt += 0
    else:
        cnt+=1

    