class genre:
    def __init__(self, i, type) -> None:
        self.ma = "TL{:03d}".format(i)
        self.type = type
        
class film:
    def __init__(self, i, maTL, date, name, leng) -> None:
        self.maP = "P{:03d}".format(i)
        self.tloai = maTL
        self.date = date
        self.name = name
        self.leng = leng
        x = ""
        for i in date.split("/"):
            x = i + x
        self.ngay = x
    def print(self):
        print(self.maP, self.tloai, self.date, self.name, self.leng)
a, b = [], []
n, m = [int(i) for i in input().split()]
for i in range(n):
    b.append(genre(i+1, input()))
for i in range(m):
    a.append(film(i+1, input(), input(), input(), int(input())))

for i in range(m):
    for j in range(n):
        if a[i].tloai == b[j].ma:
            a[i].tloai = b[j].type
a = sorted(a, key=lambda x: (x.ngay, x.name, -x.leng))
for i in a:
    i.print()
    
"""
2 3
Hai huoc
Tinh cam
TL001
25/11/2021
Phim so 1
10
TL001
04/12/2021
Phim so 2
15
TL002
25/11/2021
Phim so 3
5
"""
