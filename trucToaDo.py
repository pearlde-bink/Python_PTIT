class tdo:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
for _ in range(int(input())):
    n = int(input()) 
    a = []
    for j in range(n):
        x, y= [int(i) for i in input().split()]
        a.append(tdo(x, y))
        
    a = sorted(a, key=lambda b : b.y)
    dem = 1
    val = a[0].y
    for i in range(1, n):
        if a[i].x >= val: 
            dem += 1
            val = a[i].y
    print(dem)
    
'''
1
10
39 55
37 74
0 1
19 25
65 76
51 52
19 21
5 94
46 65
32 40
'''    