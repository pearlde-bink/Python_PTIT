def isValid(n):
    if len(n) < 3:
        return False
    i = 1
    while i < len(n) and n[i] > n[i - 1]:
        i += 1
    while i < len(n) and n[i] < n[i - 1]:
        i += 1
    return i == len(n)
    
for _ in range(int(input())):
    n = input()
    print("YES" if isValid(n) else "NO")
        
    