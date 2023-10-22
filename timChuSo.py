# IR
import math
from decimal import Decimal, getcontext
for t in range (int(input())):
    getcontext().prec = 100
    n = int(input())
    ans = Decimal(3 + math.sqrt(5)) ** n
    print("Case", end = " ")
    print("#", t + 1, ":", sep = "", end = " ")
    s = str(int(ans))
    num = len(s) - 3
    val = ""
    if num > 0: val = s[-3:]
    else: 
        for i in range(0, abs(num)):
            val += '0'
        val += s
    print(val)

    