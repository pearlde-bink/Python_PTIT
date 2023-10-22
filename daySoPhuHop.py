for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    a.sort()
    b.sort()
    
    oke = True
    for i in b:
        if oke: 
            for j in a:
                if j <= i: 
                    a.remove(j)
                    break
                else: 
                    oke = False
                    break
        else: break
    print("YES" if oke else "NO")
    