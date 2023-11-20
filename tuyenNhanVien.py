class nhanVien:
    def __init__(self, id, name, lt, th):
        self.ma = "TS0" + str(id)
        self.name = name
        if lt > 10: lt = lt / 10
        if th > 10: th = th / 10
        self.dtb  = (lt + th) / 2
        if self.dtb  < 5: self.rank = "TRUOT"
        elif self.dtb  < 8: self.rank = "CAN NHAC"
        elif self.dtb  <= 9.5: self.rank = "DAT"
        else: self.rank = "XUAT SAC"
    
    def output(self):
        print(self.ma, self.name, "{:.2f}".format(self.dtb), self.rank)
        
a = []  
n = int(input())      
for i in range(n):
    s = input()
    lt = float(input())
    th = float(input())
    a.append(nhanVien(i + 1, s, lt, th))
a = sorted(a, key=lambda x: -x.dtb)
for i in a:
    i.output()   
    
"""
3
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Pham Van Duc
56
56
""" 