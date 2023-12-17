import math
def nto(n) :
    if n < 2 : return 0
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return 0
    return 1
# a = [1] * 10001
# p = 2
# while p*p < 10001:
#     if a[p] == 1:
#         for i in range(p*p, 10001, p):
#             a[i] = 0
#     p += 1
n = int(input())
x = [int(i) for i in input().split()]
b = {}
for i in x : b[i] = 1
x = list(b)
pos = 0
for i in range(1, len(x)): x[i] += x[i-1]
for i in range(len(x)):
    if nto(x[i]) and nto(x[len(x) - 1] - x[i]):
        pos = 1
        print(i)
        break
if pos == 0: print("NOT FOUND")

'''
10
3 6 7 3 4 7 3 6 4 4
# 3 6 7 3 5 7 3 6 6 7
'''