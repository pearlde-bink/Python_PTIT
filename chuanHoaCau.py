import re
reg = '.!?'
chuanHoa = []
while True:
    try:
        s = input().lower().strip()
        kiTu = ''
        for i in s:
            if i in reg:
                kiTu = kiTu.strip()
                if len(kiTu) > 0:
                    kiTu += i
                    chuanHoa.append(kiTu)
                kiTu = ''
            else: kiTu += i
        kiTu = kiTu.strip()
        if len(kiTu) > 0: chuanHoa.append(kiTu)
    except Exception:
        break
for cau in chuanHoa:
    word = cau.split()
    val = ''
    for j in word:
        if len(j): val += j + ' '
    val = val[:len(val) - 1] #remove the last space
    if not val[-1] in reg: val += '.'
    val = val.capitalize()
    print(val)
                
                