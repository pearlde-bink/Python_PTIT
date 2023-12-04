def isValid(s):
    x = s.split(".")
    if len(x) != 4: return False
    for i in x:
        if not i.isdigit() or int(i) < 0 or int(i) > 255 : return False
    return True
    
for _ in range(int(input())):
    s = input()
    print("YES" if isValid(s) else "NO")