n, m = map(int, input().split())

seta = set(input().split())
seta = sorted(seta)
setb = set(input().split())
setb = sorted(setb)

if len(seta) != len(setb): print("NO")
else:
    oke = False
    for i in seta:
        for j in setb:
            if i == j: 
                oke = True
            break
        if oke == False:
            print("NO")
            break
    if oke: print("YES")
