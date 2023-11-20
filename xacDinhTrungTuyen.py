class tt:
    def __init__(self, id, name, mut, comp, sub) -> None:
        self.id = 'GV{:02d}'.format(id)
        self.name = name
        self.diem = comp*2 + sub + self.getUT(mut)
        self.mon = self.getSubject(mut)
        # if(self.diem >= 18): self.rank = "TRUNG TUYEN"
        # else: self.rank = "LOAI"
    def getUT(self, mut):
        if mut[1] == '1': return 2
        if mut[1] == '2': return 1.5
        if mut[1] == '3': return 1
        return 0
    def getSubject(self, mut):
        if mut[0] == 'A':  return 'TOAN'
        if mut[0] == 'B':  return 'LY'
        return 'HOA'
    def getStatus(self):
        return "TRUNG TUYEN" if self.diem >= 18 else "LOAI"
        
    def print(self):
        print(self.id, self.name, self.mon, self.diem, self.rank)
    def __str__(self) -> str:
        return '{:s} {:s} {:s} {:.1f} {:s}'.format(self.id, self.name, self.mon, self.diem, self.getStatus())

a = []
n = int(input())    
for i in range(n):
    a.append(tt(i + 1, input(), input(), float(input()), float(input())))
 
print(*sorted(a, key = lambda e: -e.diem), sep = '\n')
  
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