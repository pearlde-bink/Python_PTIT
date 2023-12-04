from itertools import combinations
n, k = [int(i) for i in input().split()]
a = set((i for i in input().split()))
a = sorted(a) #a.sort()
for i in list(combinations(a, k)):
    print(*i)
