# class sp:
#     def __init__(self, thuc, ao):
#         self.thuc = thuc
#         self.ao = ao
#     def tong(self, p):
#         re = self.thuc + p.thuc
#         unre = p.ao + self.ao
#         self.thuc = re
#         self.ao = unre
#         return self
#     def tich(self, p):
#         real = self.thuc * p.thuc - self.ao * p.ao
#         unreal = self.thuc * p.ao + self.ao * p.thuc
#         self.thuc = real
#         self.ao = unreal
#         return self
    

# for _ in range(int(input())):
#     s = [int(x) for x in input().split()]
#     a = sp(s[0], s[1])
#     b = sp(s[2], s[3])
    
#     # x = a
#     e = a.tong(b)
#     # f = e
#     c = e.tich(a)
#     d = e.tich(e)
#     print(str(c.thuc) + " + " + str(c.ao) + "i" + ", ", end = "")
#     print(str(d.thuc) + " + " + str(d.ao) + "i")
    
class sp:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def tong(self, p):
        re = self.thuc + p.thuc
        unre = p.ao + self.ao
        return sp(re, unre)

    def tich(self, p):
        real = (self.thuc * p.thuc) - (self.ao * p.ao)
        unreal = (self.thuc * p.ao) + (self.ao * p.thuc)
        return sp(real, unreal)


for _ in range(int(input())):
    s = [int(x) for x in input().split()]
    a = sp(s[0], s[1])
    b = sp(s[2], s[3])

    e = a.tong(b)
    f = e
    c = e.tich(a)
    d = f.tich(f)
    print(str(c.thuc) + " + " + str(c.ao) + "i" + ", ", end="")
    print(str(d.thuc) + " + " + str(d.ao) + "i")