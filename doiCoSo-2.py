# this method give correct answer but get IR ????
"""for t in range(int(input())):
    b = int(input())
    a = input().strip()

    result = 0

    if b == 2:
        result = a
    elif b == 8:
        octa = int(a, 2)  # conver to decimal
        result = oct(octa)  # conver to octal
        result = result[2:]  # erase prefix
    elif b == 10:
        result = int(a, 2)
    elif b == 16:
        hexa = int(a, 2)
        result = hex(hexa)
        result = result[2:]

    print(int(result))"""

# from math import log2

# BASE = '0123456789ABCDEF'
# def numberToBase(b, n):
#     step = int(log2(b)) #calculate the step size to convert into target number
#     res = '' #to contain result
#     for i in range(0, len(n), step): #loop from right to left with step = step
#         res += BASE[int(n[i:i+step][::-1], 2)]
#     return res[::-1]
# #reverse
# for r in range(int(input())):
#     print(numberToBase(int(input()), input()[::-1]))
