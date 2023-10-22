def isValid(p):
    for i in a:
        if int(i / p) == int(i / (p + 1)):
            return 0
    return 1

n = int(input())
a = [int(x) for x in input().split()]
minNum = min(a)
ans = 0
for i in range(minNum, 0, -1):
    if isValid(i):
        for num in range(n):
            ans += int(a[num] / (i + 1)) + 1
        break
print(ans)
