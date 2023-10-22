def check3(n):
    for i in n:
        if i != '0' and i != '1' and i != '2': return False
    return True
for _ in range(int(input())):
    n = input()
    print("YES" if check3(n) else "NO")