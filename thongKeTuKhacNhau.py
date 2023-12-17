ma = {}
for i in range(int(input())):
    s = input().lower()
    for j in range(len(s)):
        if not s[j].isalnum(): 
            s = s.replace(s[j], " ")
    ss = s.split()
    for i in ss:
        if i in ma:
            ma[i] += 1
        else:
            ma[i] = 1
ma = sorted(ma.items(), key = lambda x: (-x[1], x[0]))
for i in ma:
    print(i[0], i[1], sep = " ")
    # print(*i)
"""
3
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
"""    
    
    