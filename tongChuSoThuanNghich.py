def isValid(n):
    if not len(n) > 1: return False
    s = ""
    for i in range(len(n) - 1, -1, -1):
        s += n[i]
    if s != n: return False
    return True
for _ in range(int(input())):
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    print("YES" if isValid(str(sum)) else "NO")