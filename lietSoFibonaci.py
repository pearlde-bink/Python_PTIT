a = [0] * 1000
a[1] = 1
a[2] = 1
for i in range(3, 1000):
    a[i] = a[i-1] + a[i-2]
for _ in range(int(input())):
    c, b = [int(i) for i in input().split()]
    for i in range(c, b + 1):
        print(a[i], end = " ")
    print()
    
    