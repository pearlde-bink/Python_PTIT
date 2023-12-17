# import re

# for t in range(int(input())):
#     s = input()
#     print(*sorted([i for i in s if i.isalpha()]) + [sum([int(i) for i in s if i.isdigit()])], sep='')

for _ in range(int(input())):
    s = input()
    a = 0
    for i in s:
        if i.isdigit(): 
            a += int(i)
            s = s.replace(i, "")
    s = sorted(s)
    s += str(a)
    # print(''.join(s))
    for i in s:
        print(i, end = "")
    print()
'''
2
AC2BEW3
ACCBA10D2EW30
'''