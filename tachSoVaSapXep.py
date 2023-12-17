a = []
for _ in range(int(input())):
    s = input() + " "
    x = 0
    for i in range(len(s)):
        if s[i].isdigit():
           x = x*10 + int(s[i])
        elif s[i-1].isdigit():
            a.append(x)
            x = 0
a.sort()
for i in a:
    print(i)

'''
3
A129h
G07bxjq3
aaaaaaa4aaaa
'''