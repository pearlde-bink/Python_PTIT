n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
if n > m:
    a = [a[i] for i in range(n) if not (i % 2 == 0 and i // 2 < n - m)]
elif m > n:
    a = [[a[i][j] for j in range(m) if not (j % 2 == 1 and j // 2 < m - n)] for i in range(n)]
for i in a:
    print(*i)

'''
6 4
2 8 7 6
6 3 2 6
7 2 2 8
9 9 9 8
9 6 6 3
7 7 4 9

4 6
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7

4 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
'''