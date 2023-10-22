for t in range(int(input())):
    n = input()
    check = True

    for i in range(0, len(n)):
        if n[i] != '4' and n[i] != '7': 
            check = False
            break

    if check: print("YES")
    else: print("NO")
    