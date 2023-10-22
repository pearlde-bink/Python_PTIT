#cach nay bi tle :pp
"""phanNto = []

def binarySearch(arr, val):
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > val:
            result = arr[mid]
            right = mid - 1
        else:
            left = mid + 1
    return result

def uoc(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0: count += 1
    return count
        
phanNto.append(1)

for i in range(2, 1000):
    check = False
    for j in range(1, i):
        if uoc(j) < uoc(i): check = True
        else:
            check = False
            break
    if check: 
        phanNto.append(i)


for _ in range(int(input())):
    n = int(input())
    print(binarySearch(phanNto, n))"""
from bisect import bisect_left
from sys import stdin

a = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]
for __ in range(int(stdin.readline())):
    n = int(stdin.readline())
    print(a[bisect_left(a, n)])