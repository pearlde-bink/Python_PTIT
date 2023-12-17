for _ in range(int(input())):
    s = input()
    d, id = [], 1
    for i in range(len(s)):
        if s[i] == "(":
            print(id, end = " ")
            d.append(id)
            id += 1
        elif s[i] == ")":
            print(d[-1], end = " ")
            d.pop()
    print()
    
'''
2
(a + (b *c) ) + (d/e)
( ( () ) ( () ) )
'''
