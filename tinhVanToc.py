from datetime import datetime

def viettat(s):
    str = ""
    t = s.split()
    for i in t:
        str += i[0].upper()
    return str
    
class velo:
    def __init__(self, name, dvi, time):
        self.ma = viettat(dvi) + viettat(name)
        self.name = name
        self.dvi = dvi
        tg = (int(time[0]) * 60 + int(time[2:4]) - 6 * 60) / 60
        self.vtoc = 120 / tg
        self.vt = str(round(120 / tg)) + " Km/h"
    
    def output(self):
        print(self.ma, self.name, self.dvi, self.vt)
    
a = []        
for _ in range(int(input())):
    a.append(velo(input().strip(), input().strip(), input().strip()))

a = sorted(a, key=lambda x : -x.vtoc)
for i in a:
    i.output()
        
        