def vtat(s):
    x = ""
    ss = s.upper().split()
    for i in ss:
        x += i[0]
    return x
         
class vt:
    def __init__(self, ten, dvi, at) -> None:
        self.ma = vtat(dvi + " " + ten)
        self.ten = ten
        self.dvi = dvi
        self.at = at
        t = ((int(at[0]) - 6)*60 + int(at[2:4])) / 60
        self.vtoc = str(round(120/t)) + " Km/h"
    def print(self):
        print(self.ma, self.ten, self.dvi, self.vtoc)

a = []
for _ in range(int(input())):
    a.append(vt(input(), input(), input()))
a = sorted(a, key=lambda x: x.at)    
for i in a:
    i.print()
        
'''
3
Tran Vu Minh
Ha Noi
8:30
Vu Ngoc Hoang
Hoa Binh
8:20
Pham Dinh Tan
An Giang
8:45
'''       