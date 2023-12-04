for _ in range(int(input())):
    n,m = map(int, input().split())
    a = [int(i) for i in input().split()]
    a.insert(a.index(max(a)), m)
    print(*list(filter(lambda k: k < 0, a)), *list(filter(lambda k: k >= 0, a)))
    