class phongBan:
    def __init__(self, id, ten) -> None:
        self.id = id
        self.ten = ten

class nhanVien:
    def __init__(self, id, ten, lcb, ngay, phongban) -> None:
        self.id = id
        self.ten = ten
        self.lcb = lcb
        self.ngay = ngay
        self.phongban = phongban
    def heSo(self):
        nhom = self.id[0]
        nam = int(self.id[1:3])
        if nhom == 'A':
            if nam >= 1 and nam <= 3: return 10
            if nam >= 4 and nam <= 8: return 12
            if nam >= 9 and nam <= 15: return 14
            if nam >= 16: return 20
        elif nhom == 'B':
            if nam >= 1 and nam <= 3: return 10
            if nam >= 4 and nam <= 8: return 11
            if nam >= 9 and nam <= 15: return 13
            if nam >= 16: return 16
        elif nhom == 'C':
            if nam >= 1 and nam <= 3: return 9
            if nam >= 4 and nam <= 8: return 10
            if nam >= 9 and nam <= 15: return 12
            if nam >= 16: return 14
        elif nhom == 'D':
            if nam >= 1 and nam <= 3: return 8
            if nam >= 4 and nam <= 8: return 9
            if nam >= 9 and nam <= 15: return 11
            if nam >= 16: return 13
        return 0
    def getLuong(self):
        return self.lcb * self.ngay * self.heSo()
    def __str__(self) -> str:
        return f'{self.id} {self.ten} {self.phongban.ten} {self.getLuong() * 1000}'

PhongBan = []
for _ in range(int(input())):
    s = input()
    PhongBan.append(phongBan(s[:2], s[3:]))

NhanVien = []
for i in range(int(input())):        
    id = input()
    theId = id[-2:]
    for j in PhongBan:
        if j.id == theId:
            NhanVien.append(nhanVien(id, input(), int(input()), int(input()), j))
            break
print(*NhanVien, sep = '\n')
