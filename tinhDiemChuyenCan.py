class student:
    def __init__(self, msv, name, lop) -> None:
        self.msv = msv
        self.name = name
        self.lop = lop
        self.diem = 10
        self.note = ""
    def output(self):
        print(self.msv, self.name, self.lop, self.diem, self.note)

class occur:
    def __init__(self, ma, stat) -> None:
        self.ma = ma
        self.stat = stat
    def tinh(self):
        diem = 0
        s = self.stat
        for i in range(len(s)):
            if s[i] == 'm': diem += 1
            elif s[i] == 'v': diem += 2
        return diem
 
a = []      
b = []
n = int(input())
for _ in range(n):
    msv = input()
    ten = input()
    lop = input()
    a.append(student(msv, ten, lop))

for _ in range(n):
    ma, status = [x for x in input().split()]
    b.append(occur(ma, status))

for i in range(n):
    for j in range(n):
        if a[i].msv == b[j].ma:
            a[i].diem -= b[j].tinh()
            if a[i].diem < 0: a[i].diem = 0
            if a[i].diem == 0: a[i].note = "KDDK"
for i in a:
    i.output()
        
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