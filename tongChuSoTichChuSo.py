for _ in range(int(input())):
    n = input()
    sum, tich = 0, 1
    for i in range (0, len(n), 2):
        sum += int(n[i])
    check = False
    for i in range(1, len(n), 2):
        dem = 0
        if int(n[i]) == 0:
            dem += 1
        else: 
            tich *= int(n[i])
            check = True
    if not check: tich = 0
    print(sum, tich)
