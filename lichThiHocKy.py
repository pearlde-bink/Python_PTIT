class subject:
    def __init__(self, ma, ten) -> None:
        self.ma = ma
        self.ten = ten
class schedule:
    def __init__(self, i, maMon, date, hour, group) -> None:
        self.maCa = "T{:03d}".format(i+1)
        self.maMon = maMon
        self.ten = ""
        self.date = date
        self.hour = hour
        self.group = group
        x = ""
        for i in date.split("/"):
            x = i + x
        self.ss = x
    def print(self):
        print(self.maCa, self.maMon, self.ten, self.date, self.hour, self.group)
a, b = [], []
n, m = [int(i) for i in input().split()]
for i in range(n):
    b.append(subject(input(), input()))  
for i in range(m):
    e, f, g, h = input().split()
    a.append(schedule(i, e, f, g, h))    
for i in range(m):
    for j in range(n):
        if a[i].maMon == b[j].ma:
            a[i].ten = b[j].ten  
a = sorted(a, key=lambda x: (x.ss, x.hour, x.maMon))
for i in a:
    i.print()
    
"""
2 10
INT1155
Tin hoc co so 2
INT1339
Ngon ngu lap trinh C++
INT1155 25/11/2021 08:00 01
INT1155 04/12/2021 08:00 02
INT1155 04/12/2021 13:30 03
INT1155 25/11/2021 13:30 04
INT1155 25/11/2021 15:00 05
INT1339 25/11/2021 08:00 01
INT1339 25/11/2021 08:00 02
INT1339 04/12/2021 13:30 03
INT1339 04/12/2021 13:30 04
INT1339 04/12/2021 15:00 05
"""
        