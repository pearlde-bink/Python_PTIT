import re

for t in range(int(input())):
    s = input()
    print(*sorted([i for i in s if i.isalpha()]) + [sum([int(i) for i in s if i.isdigit()])], sep='')
    
# for _ in range(int(input())):
#   n = input()
#   li = []
#   tong = 0
#   for i in n:
#     if i.isdigit(): tong += int(i) 
#     else: li.append(i)
#   li = sorted(li)
#   li.append(str(tong))
#   print(''.join(li))
