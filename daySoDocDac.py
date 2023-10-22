def docnhat(n, a):
    dem = 0
    for i in range(0, n):
        if a.count(i) == 1: 
            return False
    return True
        
for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]    
    oke = True
    le = 1
    while le < n:
        if not docnhat(le, a): 
            oke = False
            break
        le += 1
    if oke: print("YES")
    else: print("NO")
    