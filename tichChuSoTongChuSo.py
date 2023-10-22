for _ in range(int(input())):
    n = input()
    sum, tich = 0, 1
    for i in range (1, len(n), 2):
        sum += int(n[i])
    # check = False
    for i in range(0, len(n), 2):
        if int(n[i]) != 0:
            tich *= int(n[i])
    print(tich, sum)
