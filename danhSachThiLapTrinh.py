class sv:
    def __init__(self, id, hoten, team, uni) -> None:
        self.msv = "C{:03d}".format(id)
        self.hoten = hoten
        self.team = team
        self.uni = uni
        
n = int(input())
t = [1]
for i in range(n):
   t.append([input(), input()])

m = int(input()) 
li = []  
for i in range(m):
    ten = input()
    team = input()
    li.append(sv(i+1, ten, t[int(team[4::])][0], t[int(team[4::])][1]))
li = sorted(li, key = lambda e: e.hoten)
for i in li:
    print(i.msv, i.hoten, i.team, i.uni)