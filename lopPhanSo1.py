import math
class ps:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def rg(self):
        d = math.gcd(self.tu, self.mau)
        self.tu //= d
        self.mau //= d
    
    def print(self):
        print(str(self.tu) + "/" + str(self.mau))
        
m, n = [int(x) for x in input().split()]
p = ps(m, n)
p.rg()
p.print()
