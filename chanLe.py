def sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def chan(n):
    check = True
    while n > 0:
        s1 = n % 10
        n //= 10
        s2 = n % 10
        if not abs(s2 - s1) == 2: 
            check = False
            break
        n //= 10
    return check

for _ in range(int(input())):
    n = int(input())
    if sum(n) % 10 == 0 and chan(n): print("YES")
    else: print("NO")