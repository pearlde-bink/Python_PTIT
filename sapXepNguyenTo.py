a = [1]*10000
e = 2
while e*e <= 10000:
    if a[e] == True:
        for i in range(e*e, 10000, e):
            a[i] = False
    e += 1
b= [] 
n = int(input())
li = [int(i) for i in input().split()]
for i in li:
    if a[i]: b += [i]
b.sort()
x = 0
for i in range(len(li)):
    if a[li[i]]: 
        li[i] = b[x]
        x += 1
print(*li)  
# import math
# def nto(n):
#     if n < 2: return False
#     else:
#         for i in range(2, math.floor(math.sqrt(n)) + 1):
#             if n % i == 0: return False
#     return True

# n = int(input())
# a = [int(i) for i in input().split()]
# b = []
# for i in range(len(a)):
#     if nto(a[i]):
#         b.append(a[i])
#         a[i] = -1
# b.sort()
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i] == -1: 
#             a[i] = b[j]
#             b.remove(b[j])
#             break
# print(*a)        
    
