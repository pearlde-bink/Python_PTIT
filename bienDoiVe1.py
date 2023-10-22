oke = True
while oke:
    n = int(input())
    if n == 0: oke = False
    else:
        if n == 1: print(1)
        else:
            dem = 1
            while n != 1:
                if n % 2 == 0: n = n / 2
                else: n = n * 3 + 1
                dem += 1
            print(dem)
    