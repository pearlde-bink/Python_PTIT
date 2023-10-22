n = int(input())
a = [int(x) for x in input().split()]
oke = True
for i in range(1, 30002):
    if not (i in a):
        print(i)
        break