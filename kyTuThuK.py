a = [0] * 1000
c = ord("A")
a[1] = "A"

for i in range(2, 27):
    a[i] = a[i-1] + chr(c + i - 1) + a[i-1]

for _ in range(int(input())):
    n, k = [int(i) for i in input().split()]
    for i in range(0, len(a[n])):
      if i == k - 1: print(a[n][i])