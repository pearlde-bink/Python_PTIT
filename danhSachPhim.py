a = {}
        
class film:
    def __init__(self, id, tag, date, name, num) -> None:
        self.id = 'P{:03d}'.format(id)
        self.tag = self.filmType(tag)
        self.name = name
        self.date = date
        self.num = num
        t = date.split('/')
        s = ""
        for i in range(len(t) - 1, -1, -1):
            s += t[i] 
        self.ssDate = s  #to compare film by date
    
    def filmType(self, tag):
        s = ""
        for i in a:
            if tag == a[i]:
                s = i
        return s
    
    def print(self):
        print(self.id, self.tag, self.date, self.name, self.num)

b = []
n, m = map(int, input().split())
for i in range(n):
    s = input()
    a[s] = 'TL{:03d}'.format(i+1)

for i in range(m):
    b.append(film(i+ 1, input(), input(), input(), int(input()))) 
b = sorted(b, key = lambda x: (x.ssDate, x.name, -x.num))
for i in b:
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
