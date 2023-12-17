import re
from sys import stdin

res = ''
ipStr = stdin.readlines()
for line in ipStr:
    res += re.sub('[\.\?\!]+', '\n', ' '.join(re.split('\\s+', line.strip().lower())))
for i in (re.split('\n\s?', res)):
    if i != '':
        print(i[0:1].upper() + i[1:])   

'''
ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!
    vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11.
'''    