reg = ".!?"
chuanHoa = []
while True:
    try:
        s = input().lower().strip()
        kitu = ""
        for i in s:
            if i in reg:
                kitu = kitu.strip()
                kitu += i
                chuanHoa.append(kitu)
                kitu = ""
            else: kitu += i
        kitu = kitu.strip()
        if len(kitu) > 0: chuanHoa.append(kitu)
    except Exception:
        break
for cau in chuanHoa:
    ss = cau.split()
    val = ""
    for i in ss:
        val += i + " "
    val = val[:len(val)-1]
    if not val[-1] in reg: val += "."
    print(val.capitalize())
 
'''
Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te.    
co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin
muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep
moi    CAC BAN danG ky     thaM giA !
'''   