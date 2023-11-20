import functools
from decimal import ROUND_HALF_UP, Decimal

id = 1

class hs:
    ma = 'HS'
    dtb = 0
    rank = ''
    def __init__(self, ten, diem):
        global id
        self.ma += '{:02d}'.format(id)
        id += 1
        self.ten = ten
        x = (diem[0] + diem[1]) * 2
        for i in range(2, 10):
            x += diem[i]
        x /= 12
        if x < 5: self.rank = "YEU"
        elif x < 7: self.rank = "TB"
        elif x < 8: self.rank = "KHA"
        elif x <9: self.rank = "GIOI"
        else: self.rank = "XUAT SAC"
        self.dtb = x.quantize(Decimal('0.1'), ROUND_HALF_UP)
    
    def print(self):
        print(self.ma, self.ten, self.dtb, self.rank)

def cmp(h1, h2):
    if h1.dtb < h2.dtb: return 1
    elif h1.dtb > h2.dtb: return -1
    else:
        if h1.ma < h2.ma: return -1
        elif h1.ma > h2.ma: return 1

a = []        
for _ in range(int(input())):
    s = input()
    b = [Decimal(x) for x in input().split()]
    a.append(hs(s, b))
    
# a = sorted(a,  key = functools.cmp_to_key(cmp))
a = sorted(a, key = lambda x: (-x.dtb, x.ma))
for i in a:
    i.print()
        
"""
3
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
"""            
