# import math
for _ in range(int(input())):
    s1 = input()
    s2 = "" #s2 = s1[::1]
    for i in s1:
        s2 = i + s2
    check = True
    for i in range(len(s1)):
        #ord to convert to ASCII
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
            check = False
            break
    if check: print("YES")
    else: print("NO")