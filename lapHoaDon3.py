# class bill:
#     def __init__(self, id, name, num, price, disc) -> None:
#         self.id = id
#         self.name = name
#         self.num = num
#         self.price = price
#         self.disc = disc
#     def total(self):
#         return self.num * self.price - self.disc
#     def print(self):
#         print(self.id, self.name, self.num, self.price, self.disc, self.total())
        
# a = []
# for _ in range(int(input())):
#     a.append(bill(input(), input(), int(input()), int(input()), int(input())))
# a = sorted(a, key = lambda x: -x.total())
# for i in a:
#     i.print()

class bill:
    def __init__(self, id, ten, slg, dg, ck) -> None:
        self.id = id
        self.ten = ten
        self.slg = slg
        self.dg = dg
        self.ck = ck
        self.tien = slg*dg - ck
    def print(self):
        print(self.id, self.ten, self.slg, self.dg, self.ck, self.tien)
a = []
for i in range(int(input())):
    a.append(bill(input(), input(), int(input()), int(input()), int(input())))
a = sorted(a, key=lambda x: -x.tien)
for i in a:
    i.print()
"""
3
ML01
May lanh SANYO
12
4000000
2400000
ML02
May lanh HITACHI
4
2550000000
0
ML03
May lanh NATIONAL
5
3000000
150000
"""
             