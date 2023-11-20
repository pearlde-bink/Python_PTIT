tho = [len(input().split()) for i in range(int(input()))]
ds = []
i = 0
while i < len(tho):
    if tho[i] == 7:
        i += 4
        ds += [2]
    elif tho[i] == 6:
        i += 2
        ds += [1]
        while i < len(tho) and tho[i] == 6:
            i += 2
print(len(ds), *ds, sep='\n')