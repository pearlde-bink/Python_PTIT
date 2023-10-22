out = []
def exist(li, val):
    found = False
    for i, row in enumerate(li):
        for j, element in enumerate(row):
            if element == val:
                found = True
                s = "Vi tri [{}][{}]".format(i, j)
                out.append(s)
    return found

n, m = map(int, input().split())

minNum = 10000
maxNum = -1000
a = []

for _ in range(n):
    b = list(map(int, input().split()))
    minNum = min(min(b), minNum)
    maxNum = max(max(b), maxNum)
    a.append(b)

val = maxNum - minNum
oke = False

if exist(a, val):
    print(val)
    for i in out:
        print(i)
else: print("NOT FOUND")