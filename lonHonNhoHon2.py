from sys import stdin, setrecursionlimit

input = stdin.readline
arr, ten = [], set()
n = int(input())

for i in range(n):
    ten1, dau, ten2 = input().split()
    ten.add(ten1)
    ten.add(ten2)
    
    if dau == '>': arr.append((ten1, ten2))
    else: arr.append((ten2, ten1))
    
a = sorted(ten)
m = len(a)

def ind(Ten):
    l, r = 0, m
    while l < r:
        mid = (l + r) >> 1
        if a[mid] == Ten: return mid
        if a[mid] < Ten: l = mid + 1
        else: r = mid
    return -1

canh = [[] for i in range(m)]
for n1, n2 in arr: canh[ind(n1)].append(ind(n2))
auth = [0]*m
setrecursionlimit(10**6)
def dfs(i):
    auth[i] = 1
    for j in canh[i]:
        if auth[j] == 0:
            if(dfs(j)): return True
        if auth[j] == 1: return True
    auth[i] = 2
    return False

oke = False
for i in range(m):
    if auth[i] == 0:
        if dfs(i): 
            oke = True
            break
if oke: print('impossible')
else: print('possible')

    
