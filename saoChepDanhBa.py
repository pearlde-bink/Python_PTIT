class danhBa:
    def __init__(self, name, sdt, date) -> None:
        self.name = name
        self.sdt = sdt
        self.date = date
        self.firstName = name.split()[-1]
    def __str__(self) -> str:
        return f'{self.name}: {self.sdt} {self.date}'

f = open("SOTAY.txt", 'r')
date = ''
li = []
try:
    while f:
        s = next(f).strip()
        if s.startswith("Ngay"): date = s[5:]
        else:
            li.append(danhBa(s, next(f).strip(), date))
except StopIteration:
    f.close()
    
li.sort(key = lambda e: (e.firstName, e.name))
dt = open("DIENTHOAI.txt", 'w')
dt.write('\n'.join([str(i) for i in li]))
dt.close()
