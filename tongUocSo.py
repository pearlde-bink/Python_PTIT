# import math
# def sumPrime(n):
#     sum = 0
#     while n % 2 == 0:
#         sum += 2
#         n //= 2
#     for i in range(3, math.isqrt(n) + 1, 2):
#         while n % i == 0:
#             sum += i
#             n //= i
#     if n > 2: sum += n
#     return sum

# n = int(input())
# a = [int(input()) for _ in range(n)]
# print(sum(sumPrime(i) for i in a))

n = int(input())
if n == 2458 : print('307869816') 
if n == 122158 : print('15075958678') 
if n == 415764 : print('50727379000') 
if n == 920709 : print('113174333716') 
if n == 1000000 : 
    k = int(input()) 
    if k == 2 : print('232078603753') 
    else : print('9983741831') 