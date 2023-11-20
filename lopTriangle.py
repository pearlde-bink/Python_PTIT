import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, p2):
        f = math.sqrt(math.pow((p2.x - self.x), 2) + math.pow((p2.y - self.y), 2))
        return f

class Triang:
    def __init__(self, m, h, b):
        self.m = m
        self.h = h
        self.b = b
    def chuvi(self):
        c1 = self.m.distance(self.h)
        c2 = self.h.distance(self.b)
        c3 = self.b.distance(self.m)
        if max(c1, c2, c3) * 2 >= (c1 + c2 + c3): print("INVALID")
        else: print("{:.3f}".format(c1 + c2 + c3)) 
       
a = []
t = int(input())
for _ in range(t):
    a += [float(x) for x in input().split()]
i = 0  
for ind in range(t):
    mot = Point(a[i], a[i+1])   
    hai = Point(a[i+2], a[i+3])    
    ba = Point(a[i+4], a[i+5])   
    i += 6
    tri = Triang(mot, hai, ba)
    tri.chuvi()
