n = input()
hoa, thuong = 0, 0
for i in range(0, len(n)):
    if n[i].isupper(): hoa += 1
    else: thuong += 1
if hoa > thuong: print(n.upper())
else: print(n.lower())