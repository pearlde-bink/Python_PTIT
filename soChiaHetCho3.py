def chia3(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
for _ in range(int(input())):
    n = int(input())
    if chia3(n) % 3 == 0: print("YES")
    else: print("NO")
