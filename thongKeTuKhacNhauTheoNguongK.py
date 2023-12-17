n, k = [int(i) for i in input().split()]
a = {}
for _ in range(n):
    s = input().lower()
    for i in range(len(s)):
        if not s[i].isalnum():
            s = s.replace(s[i], " ")
    for i in s.split():
        if not i in a: a[i] = 1
        else: a[i] += 1
a = sorted(a.items(), key = lambda x: (-x[1], x[0]))
for x, y in a:
    if y >= k:
        print(x, y, sep = " ")
'''
3 2
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
'''
    