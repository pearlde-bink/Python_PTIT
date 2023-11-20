import math
class ps:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def rg(self):
        k = math.gcd(self.tu, self.mau)
        self.tu //= int(k)
        self.mau //= int(k)
    
    def add(self, x):
        a = self.tu * x.mau + self.mau * x.tu
        b = self.mau * x.mau
        self.tu = a
        self.mau = b
    
    def print(self):
        print(str(self.tu) + "/" + str(self.mau))
        
m, n, q, r = [int(x) for x in input().split()]
p = ps(m, n)
p2 = ps(q, r)
p.add(p2)
p.rg()
p.print()
