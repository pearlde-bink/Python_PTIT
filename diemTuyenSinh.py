class thiSinh:
    def __init__(self, id, ten, diem, dtoc, kvuc) -> None:
        self.id = 'TS{:02d}'.format(id)
        self.diem = diem + self.congDanToc(dtoc) + self.congVung(kvuc)
        self.ten = self.formatName(ten)
        self.kqua = 'Do' if self.diem >= 20.5 else 'Truot'
    def formatName(self, ten) -> str:
        return ' '.join(i.capitalize() for i in ten.strip().split())
    def congDanToc(self, dtoc):
        if dtoc == 'Kinh': return 0
        else: return 1.5
    def congVung(self, kvuc):
        if kvuc == '1': return 1.5
        elif kvuc == '2': return 1
        return 0
    def __str__(self) -> str:
        return '{:s} {:s} {:.1f} {:s}'.format(self.id, self.ten, self.diem, self.kqua)
        
list = []
for i in range(int(input())):
    list.append(thiSinh(i+1, input(), float(input()), input(), input()))
print(*sorted(list, key = lambda e: (-e.diem, e.id, e)), sep = '\n')
    