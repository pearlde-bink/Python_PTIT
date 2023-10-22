def isValid(n):
    for i in n:
        if int(i) % 2 != 0: return False
    if len(n) % 2 != 0: return False
    s = ""
    for i in range(len(n) - 1, -1, -1):
        s += n[i]
    if s != n: return False
    return True
for _ in range(int(input())):
    n = input()
    for i in range(22, int(n), 2):
        if isValid(str(i)):
            print(i, end = " ")
    print()