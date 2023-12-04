import math
def prime(n):
    if n < 2: return 0
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0: return 0
    return 1

def uocNto(n):
    a = []
    for i in range(0, n + 1):
        if prime(i) and n % i == 0: a.append(i)
    return a

nto = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

while True:
    # l, r = [int(i) for i in input().split()]
    l, r = map(int, input().split())
    if l == -1: break
    n = int(input())
    cnt = 0
    if l == 1: cnt += 1
    if l < n: l = n #cac so nho hon n chac chan bi chia het
    for i in range (l + 1, r+1): 
        if prime(i): #neu la nto thi khong bi chia het trong [2, N]
            cnt += 1
            continue
        else:       #neu khong phai nto
            a = uocNto(i)  #tao list uoc nto 
            oke = True
            for j in nto: #ktra neu uoc cua i la so nto trong [2, 50]
                if j in a: 
                    oke = False
                    break
            if oke == True: cnt += 1
    print(cnt)
# def sieve_of_eratosthenes(limit):
#     primes = [True] * (limit + 1)
#     primes[0] = primes[1] = False
#     for i in range(2, int(limit**0.5) + 1):
#         if primes[i]:
#             for j in range(i*i, limit + 1, i):
#                 primes[j] = False
#     return [x for x in range(limit + 1) if primes[x]]

# def inclusion_exclusion_principle(L, R, N):
#     primes = sieve_of_eratosthenes(N)
#     result = R - L + 1  # Ban đầu giả sử tất cả các số từ L đến R đều thỏa mãn

#     for i in range(1, 1 << len(primes)):  # Duyệt qua tất cả các tập con của các số nguyên tố
#         product = 1
#         count_bits = 0
#         for j in range(len(primes)):
#             if (i >> j) & 1:
#                 count_bits += 1
#                 product *= primes[j]

#         if count_bits % 2 == 1:
#             result -= (R // product) - ((L - 1) // product)

#         else:
#             result += (R // product) - ((L - 1) // product)

#     return result

# # Đọc input
# while True:
#     L, R = map(int, input().split())
#     if L == -1:
#         break
#     N = int(input())

#     # In kết quả
#     print(inclusion_exclusion_principle(L, R, N))
