def phi(s):
    if s[3] == "OUT": return 0
    if s[1] == "Xe_con" and s[2] == "5": return 10000
    if s[1] == "Xe_con" and s[2] == "7": return 15000
    if s[1] == "Xe_tai" and s[2] == "2": return 20000
    if s[1] == "Xe_khach" and s[2] == "29": return 50000
    if s[1] == "Xe_khach" and s[2] == "45": return 70000

dict = {}
for _ in range(int(input())):
    s = [i for i in input().split()]
    if dict.get(s[-1]) == None:
        dict.update({s[-1] : phi(s)})
    else: dict.update({s[-1] : dict.get(s[-1]) + phi(s)})
for k, v in dict.items():
    print(k, v, sep = ": ")
