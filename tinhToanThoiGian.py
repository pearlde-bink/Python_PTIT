class tgian:
    def __init__(self, id, name, vao, ra) -> None:
        self.id = id
        self.name = name
        x = int(ra[0:2]) * 60 + int(ra[3:5]) - int(vao[0:2]) * 60 - int(vao[3:5])
        self.gio = x
        self.hour = str(x // 60) + " gio " + str(x % 60) + " phut"
        
    def output(self):
        print(self.id, self.name, self.hour)
      
a = []  
for _ in range(int(input())):
    s = input()
    ten = input()
    va = input()
    ra = input()
    a.append(tgian(s, ten, va, ra))

a = sorted(a, key=lambda x: -x.gio)
for i in a:
    i.output()

"""
3
01T
Nguyen Van an
09:00
10:30
06T
Hoang Van Nam
15:30
18:00
02I
Tran Hoa Binh
09:05
10:00
"""
        