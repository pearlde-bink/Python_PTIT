# import math
# def prime(n):
#     if n < 2: return False
#     else:
#         for i in range(2, math.isqrt(n) + 1):
#             if n % 2 == 0: return False
#     return True
    
# a = []
# a.append(0)
# a.append(1)
# dem = 1 
# for i in range(2, 1000): #loop to insert into hamming array
#     val = 0 #assign to biggest divisor
#     res = i
#     for j in range(2, i+1): #loop to find biggest prime divisor
#         if prime(j):
#             while i > 0 and i % j == 0:
#                 val = j
#                 i //= j
#     if val <= 5: 
#       dem += 1
#       a.insert(dem, res)

# for _ in range(int(input())):
#     n = int(input())
#     if n in a: 
#         print(a.index(n))
#     else: 
#         print("Not in sequence")

ham = {1 : 1}
while True :
    ok = 0
    a = []
    for i in ham :
        if i < 10**18 :
            if not((i * 2) in ham) :
                a.append(i * 2)
            if not((i * 3) in ham) :
                a.append(i * 3)
            if not((i * 5) in ham) :
                a.append(i * 5)
    for i in a :
        ok = 1
        ham[i] = 1
    if ok == 0 : break
pos = 1
a = sorted(list(ham))
for i in a :
    ham[i] = pos
    pos += 1
t = int(input())
for i in range(t) :
    n = int(input())
    if n in ham : print(ham[n])
    else : print("Not in sequence")
