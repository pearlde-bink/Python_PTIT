def reverse(n):
    if n < 10: return n
    else:
        dao = 0
        while n > 0:
            dao = dao * 10 + n % 10
            n //= 10
    return dao

for _ in range(int(input())):
    n = int(input())
    bool = False
    dem = 0
    i = n
    while dem < 1000:
        if i % 7 == 0:
            bool = True
            print(i)
            break
        elif (i + reverse(i)) % 7 == 0:
            bool = True
            print(i + reverse(i))
            break
        else: i += reverse(i)
    if not bool: print("-1")
        
    