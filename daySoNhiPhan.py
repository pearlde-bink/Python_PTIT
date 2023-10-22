n = int(input())
count = 0
a = [int(x) for x in input().split()]
for i in range(len(a) - 1):
    if a[i] != a[i+1]: count += 1
print(count)
    