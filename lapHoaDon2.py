from datetime import datetime

class hotel:
    def __init__(self, id, name, room, dayIn, dayOut, extra) -> None:
        self.ma = "KH" + "{:02d}".format(id)
        self.name = name
        self.room = room
        dIn = datetime.strptime(dayIn, '%d/%m/%Y').date()
        dOut = datetime.strptime(dayOut, '%d/%m/%Y').date()
        self.day = (dOut - dIn).days
        self.day += 1
        if self.room[0] == "1": self.price = self.day * 25 + extra
        elif self.room[0] == "2": self.price = self.day * 34 + extra
        elif self.room[0] == "3": self.price = self.day * 50 + extra
        else: self.price = self.day * 80 + extra
        
    def output(self):
        print(self.ma, self.name, self.room, self.day, self.price)
    
a = []
for i in range(int(input())):
    a.append(hotel(i+1, input().strip(), input().strip(), input().strip(), input().strip(), int(input().strip())))

a = sorted(a, key=lambda x: -x.price)
for i in a:
    i.output()

"""
3
Huynh Van Thanh
103
05/06/2010
05/06/2010
15
Le Duc Cong
106
08/03/2010
01/05/2010
220
Tran Thi Bach Tuyen
207
10/04/2010
21/04/2010
96
"""