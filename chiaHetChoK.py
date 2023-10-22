# a, k, n = [int(i) for i in input().split()]

# l = (int(a / k) + 1) * k - a #boi so tiep theo cua k lon hon a
# r = (int(n / k)) * k - a #boi gan k nhat cua n ma nho hon a

# if l > r: print(-1)
# else: 
#     for i in range (l, r + 1, k):
#         print(i, end = " ")

a, K, N = map(int, input().split())

if a >= N or a % K == 0: print(-1)
else:
    first_b = ((a // K) + 1) * K - a #gt min cua b tman a + b <= n and a + b % k == 0
    max_b = N - a

    if first_b <= max_b:
        for b in range(first_b, max_b + 1, K):
            print(b, end=' ')
    else:
        print(-1)
