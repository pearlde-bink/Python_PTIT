import sys

li = []
f =  open('DATA.in')
for i in f:
    for j in i.split():
        if (not j.isdigit()) or int(j) > sys.maxsize:
            li.append(j)
print(*sorted(li, key = lambda e: e))