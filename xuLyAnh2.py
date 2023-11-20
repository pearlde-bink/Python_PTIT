for _ in range(int(input())):
    n, m, l = [int(x) for x in input().split()]
    a = [[0] * (m + 1)] * (n + 1)
    for i in range(1, n + 1):
        a[i] = [0] + [int(x) for x in input().split()]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a[i][j] += a[i][j-1] + a[i-1][j] - a[i-1][j-1]
    for i in range(1, n - l + 2):
        for j in range(1, m - l + 2):
            k = int((a[i + l - 1][j + l - 1] - a[i - 1][j + l - 1] - a[i + l - 1][j - 1] + a[i - 1][j - 1]) / (l * l))
            print(k, end = " ")
        print()    
"""        
2
4 4 3
2 1 0 0
3 2 1 1
4 5 2 1
2 2 9 0
3 3 3
1 2 3
4 5 6
7 8 9
"""