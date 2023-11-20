
id = 1
class kh:
    tien = 0
    ma = "KH"
    
    def __init__(self, name, bef, aft):
        global id
        self.ma += "{:02d}".format(id)
        id += 1
        self.name = name
        m3 = aft - bef
        x = 0
        if m3 <51: x = m3 * 102
        elif m3 < 101: x = (50 * 100 + (m3 - 50) * 150 ) * 1.03
        else: x = (50 * 100 + 50 * 150 + (m3 - 100) * 200 ) * 1.05
        self.tien = round(x) 
        
    def output(self):
        print(self.ma, self.name, self.tien)
        
a = []
for _ in range(int(input())):
    s = input()
    bef = int(input())
    aft = int(input())
    a.append(kh(s, bef, aft))

a = sorted(a, key = lambda x : (-x.tien))
for i in a:
    i.output()

"""
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
"""
    