class gv:
    def __init__(self, id, ten, mxt, tin, cmon) -> None:
        self.ma = "GV{:02d}".format(id)
        self.ten = ten
        if mxt[0] == 'A': self.monhoc = "TOAN"
        elif mxt[0] == 'B': self.monhoc = "LY"
        else: self.monhoc = "HOA"
        self.diem = tin*2 + cmon
        if mxt[1] == '1': self.diem += + 2
        elif mxt[1] == '2': self.diem += 1.5
        elif mxt[1] == '3': self.diem += 1
        # else: self.diem = tin*2 + cmon
        if self.diem >= 18: self.stat = "TRUNG TUYEN"
        else: self.stat = "LOAI"
    def print(self):
        print(self.ma, self.ten, self.monhoc, self.diem, self.stat)

a = []
for i in range(int(input())):
    a.append(gv(i+1, input(), input(), float(input()), float(input())))
a = sorted(a, key=lambda x: -x.diem)
for i in a:
    i.print()
 
"""
3   
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
"""      