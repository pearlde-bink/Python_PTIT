import math
class sinhVien:
    def __init__(self, id, name, d1, d2, d3) -> None:
        self.id = 'SV{:02d}'.format(id)
        self.name = self.chuan(name)
        self.tb = (d1*3 + d2*3+ d3*2) / 8
    
    def chuan(self, name):
        return ' '.join(i.title() for i in name.strip().split())
        
    def print(self):
        print(self.id, self.name, round(math.ceil(self.tb * 100) / 100, 2), self.rank)
    def __str__(self) -> str:
        return '{:s} {:s} {:.2f} {:d}'.format(self.id, self.name, math.ceil(self.tb*100)/100, self.rank)
a = []
for i in range(int(input())):
    a.append(sinhVien(i+1, input(), float(input()), float(input()), float(input())))
a = sorted(a, key=lambda x: (-x.tb, x.id))
a[0].rank = 1
for i in range(1, len(a)):
    a[i].rank = a[i-1].rank if a[i].tb == a[i-1].tb else i + 1
# for i in a:
#     i.print()
print(*a, sep='\n')
"""
2
 ha Thi kieu     anh
7
6
7
Pham    THI  HAO
6
7
6
"""