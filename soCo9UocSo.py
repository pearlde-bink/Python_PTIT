from math import sqrt

res, n = 0, int(input())
m = int(sqrt(n)) + 1

p = [i for i in range(m)] #p[i] là ước nt của i
for i in range(2, int(sqrt(m))):
    if p[i] == i:
        for j in range(i*i, m, i):
            if p[j] == j: p[j] = i

for i in range(2,m):
    i1 = p[i]
    i2 = i // i1
    if i2 == p[i//i1] and i1 != i2 and i2 != 1:  # kiểm tra i là tích của 2 snt
        res += 1
    elif p[i] == i and pow(i, 8) <= n:  
        res += 1        

print(res)

#cach nay ra kqua dung nhung bi IR
'''from math import sqrt
up = 100000
prime = [True for i in range (up+1)]
def sieveNum():
  prime[0], prime[1] = False, False
  i = 2
  while i*i <= up + 1:
    if prime[i]:
      for j in range(i*i, up+1, i):
        prime[j] = False
    i += 1

def countDivisor(n):
  cnt = 0
  for i in range(1, int(sqrt(n) + 1)):
    if n % i == 0: 
      if i * i != n: cnt += 2 
      else: cnt += 1
  return cnt

sieveNum()
n = int(input())
cnt = 0
for i in range(36, n+1):
  if not prime[i] and countDivisor(i) == 9: 
    cnt += 1

print(cnt)
'''
