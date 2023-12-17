def tn(s):
    if len(s) >= 2 and s == s[::-1]: return True
    return False

n, m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for i in range(n)]
val = 0
for i in range(n):
    for j in range(m):
        if tn(str(a[i][j])):
            val = max(val, a[i][j])
if val == 0: print("NOT FOUND")
else:
    print(val)
    for i in range(n):
        for j in range(m):
            if a[i][j] == val:
                print(f'Vi tri [{i}][{j}]')
'''
6 4
23 21 77 10
13 13 22 14
28 29 28 23
29 77 11 19
16 26 24 21
13 25 77 77
'''