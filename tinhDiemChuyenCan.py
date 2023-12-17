class hs:
    def __init__(self, msv, ten, lop) -> None:
        self.msv = msv
        self.ten = ten
        self.lop = lop
        self.diem = 10
        self.stat = ""
    def print(self):
        print(self.msv, self.ten, self.lop, self.diem, self.stat)
        
class occur:
    def __init__(self, ma, tt) -> None:
        self.ma = ma
        self.tt = tt
    def sub(self):
        diem = 0
        for i in range(len(self.tt)):
            if self.tt[i] == 'm': diem += 1
            elif self.tt[i] == 'v': diem += 2
        return diem
    
a, b = [], []
n = int(input())
for _ in range(n):
    a.append(hs(input(), input(), input()))
for _ in range(n):
    m, mm = [i for i in input().split()]
    b.append(occur(m, mm))
for i in range(len(a)):
    for j in range(len(b)):
        if a[i].msv == b[j].ma:
            a[i].diem -= b[j].sub()
            if a[i].diem <= 0: 
                a[i].diem = 0
                a[i].stat = "KDDK" 
for i in a:
    i.print()
        
"""
3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
"""       