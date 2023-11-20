for _ in range(int(input())):
    n = int(input())
    a = [0] * n
    b = [0] * n
    so = [1] * n
    val = 1
    for i in range(n): 
        a[i], b[i] = [float(x) for x in input().split()] 
    for i in range(n):
        for j in range(0, i):
            if a[i] > a[j] and b[i] < b[j]:
                so[i] = max(so[i], so[j] + 1)
        val = max(val, so[i])
    print(val)