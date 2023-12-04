class Ielts:
    def conv(self, diem):
        if diem <= 4: return 2.5
        if diem <= 6: return 3
        if diem <= 9: return 3.5
        if diem <= 12: return 4
        if diem <= 15: return 4.5
        if diem <= 19: return 5
        if diem <= 22: return 5.5
        if diem <= 26: return 6
        if diem <= 29: return 6.5
        if diem <= 32: return 7
        if diem <= 34: return 7.5
        if diem <= 36: return 8
        if diem <= 38: return 8.5
        if diem <= 40: return 9
        return 0

    def __init__(self, read, lis, speak, wri) -> None:
        self.read = self.conv(read)
        self.lis = self.conv(lis)
        self.speak = speak
        self.wri = wri
        self.score = (self.read + self.lis + self.speak + self.wri) / 4

    def round2(self, n):
        a = n - int(n)
        if a >= 0.75:
            return int(n) + 1
        elif a >= 0.25:
            return int(n) + 0.5
        return int(n)

    def __str__(self) -> str:
        return '{:.1f}'.format(self.round2(self.score))

for _ in range(int(input())):
    li = [float(i) for i in input().split()]
    print(Ielts(li[0], li[1], li[2], li[3]))


