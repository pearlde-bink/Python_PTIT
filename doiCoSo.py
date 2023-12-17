base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    val = ""
    while n:
        val += base[n%m]
        n //= m
    print(val[::-1])
'''
3
10 2
2021 2
31 16
'''