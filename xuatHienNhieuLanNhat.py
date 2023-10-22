for _ in range(int(input())):
    n = int(input())
    di = {}
    a = input().split()
    s = 0
    for x in a:
        if x in di: di[x] += 1
        else: di[x] = 1
    for i in a:
        if s < di[i]:
            s = di[i]
            p = i
    if s > n / 2: print(p)
    else: print("NO")

    
        