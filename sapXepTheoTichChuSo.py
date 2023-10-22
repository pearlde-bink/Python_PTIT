def tichChuSo(n):
    sum = 1
    while n > 0:
        sum *= n % 10
        n //= 10
    return sum
        

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a)
    a.sort(key=lambda i: tichChuSo(i))
    print(*a)
    
    