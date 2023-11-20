a = {}
class schedule:
    def __init__(self, id, maMon, day, hour, group) -> None:
        self.maCa = 'T{:03d}'.format(id)
        self.maMon = maMon
        self.mon = self.sub(maMon)
        self.day = day
        t = day.split("/")
        s = ""
        for i in range(len(t) - 1, -1, -1):
            s += t[i]
        self.ssDate = s
        self.hour = hour
        self.group = group
    
    def sub(self, maMon):
        s = ""
        for i in a:
            if maMon == i: s = a[i]
        return s
    
    def print(self):
        print(self.maCa, self.maMon, self.mon, self.day, self.hour, self.group)
        
b = []
n, m = map(int, input().split())
for i in range(n):
    s1 = input() #ma
    s2 = input() #ten mon hoc
    a[s1] = s2
for i in range(m):
    s = input()
    t = s.split()
    t1 = t[0]
    t2 = t[1]
    t3 = t[2]
    t4 = t[3]
    b.append(schedule(i+1, t1, t2, t3, t4))
b = sorted(b, key=lambda x: (x.ssDate, x.hour, x.maMon))
for i in b:
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
        