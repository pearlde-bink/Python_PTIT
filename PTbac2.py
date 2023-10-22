import math
a = int(input())
b = int(input())
c = int(input())

denta = b**2 - 4 * a * c
if(a == 0) :
    if(b == 0):
        if(c != 0): print("PT vo nghiem")
        else: print("PT vo so ngiem")
    else:
        if(c == 0): print(0)
        else: print(-c / b)
else:
    if denta < 0: print("PT vo nghiem")
    elif denta == 0: print(-b / (2 * a))
    elif denta > 0:
        print((-b + math.sqrt(denta)) / (2 * a))
        print((-b - math.sqrt(denta)) / (2 * a))

