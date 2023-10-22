n = int(input())
a = [float(x) for x in input().split()]
a = sorted(a)
sum, dem = 0, 0
for i in range(1, len(a) - 1):
    if a[i] != a[0] and a[i] != a[len(a) - 1]:
        dem += 1
        sum += a[i]
print("{:.2f}".format(sum / dem))

