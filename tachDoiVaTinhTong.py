s = input()
while len(s) > 1:
    s = str(int(s[:len(s)//2]) + int(s[len(s)//2:]))
    print(s)