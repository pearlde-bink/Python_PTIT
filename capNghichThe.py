n = int(input())
a = [int(x) for x in (input().split())]
dem = 0

for i in range(len(a) - 1):
    for j in range(i+1,len(a)):
        if a[i] > a[j]: dem += 1
print(dem)
