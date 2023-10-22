for t in range(int(input())):
    n = input()
    dau = n[0] + n[1]
    cuoi = n[len(n) - 2] + n[len(n) - 1]
    if(int(dau) == int(cuoi)): print("YES")
    else: print("NO")