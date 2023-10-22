from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    di = dict()
    for x in a:
        di.update({x: a.count(x)})
    s = 0
    for i in di:
        if di[i] > s:
            s = di[i]
            p = i
        elif di[i] == s:
            p = min(p, i)
    print(p)
    
    