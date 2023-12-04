while(True):
    n = int(input())
    if n == 0: break
    else:
        s = []
        for i in range(n):
            s += [int(input())]
        s = sorted(list(set(s)))
        if len(s) > 1: print(s[0], s[len(s) - 1], sep = " ")
        else: print("BANG NHAU")
    