for __ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    x = [[int(j) for j in input().split()] for i in range(n)]
    h = [[int(j) for j in input().split()] for i in range(3)]

    y = [[sum(h[k][l] * x[i+k][j+l] for l in range(3) for k in range(3)) for j in range(m-2)] for i in range(n-2)]
    print(sum([sum(i) for i in y]))

    
'''
2
4 4
2 1 0 0
3 2 1 1
4 3 2 1
2 2 1 0
-1 -1 -1
-1 8 -1
-1 -1 -1
3 3
1 2 3
4 5 6
7 8 9
1 1 1
1 1 1
1 1 1
'''    