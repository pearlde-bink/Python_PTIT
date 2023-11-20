def uuThe(n):
    cnt = 0
    m = n
    while n > 0:
        k = n % 10
        if k == 2: cnt += 1
        elif k != 1 and k != 0: return False
        n //= 10
    if n == 2: cnt += 1
    if cnt > len(str(m)) / 2: return True
    return False

a = []
for i in range(2, 10000):
    if uuThe(i) == 1: a.append(i)

for _ in range(int(input())):
    n = int(input())
    for i in range(0, n):
        print(a[i], end = " ")
    print()