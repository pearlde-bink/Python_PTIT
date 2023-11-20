base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    result = ""
    while n:
        result += base[n%m]
        n //= m
    print(result[::-1])
    