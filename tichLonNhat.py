n = int(input())
val = 0
a = sorted([int(i) for i in input().split()])
m1 = a[-1] * a[-2]
m2 = a[-1] * a[-3] * a[-2]
m3 = a[0] * a[1]
m4 = a[-1] * a[0] * a[1]
val = max(m1, m2, m3, m4)
print(val)

        
