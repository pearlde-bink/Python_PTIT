for _ in range(int(input())):
    n = input()
    s = n[::-1]
    check = True
    for i in range(1, len(n)):
        if not abs(ord(n[i]) - ord(n[i-1])) == abs(ord(s[i]) - ord(s[i-1])):
            check = False
            break
    print("YES" if check else "NO")
    
    