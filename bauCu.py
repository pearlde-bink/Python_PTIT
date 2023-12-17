n,m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
dic = {}
for i in a:
    if dic.get(i) == None:
        dic.update({i:1})
    else:
        dic.update({i:dic.get(i)+1})

dic = sorted(dic.items(), key = lambda x : (-x[1], x[0]))
val = dic[0][1]
pos, j = 0, 0
for i in dic:
    if i[1] < val: 
        val = i[1]
        pos = j
        break
    j += 1
if val != dic[0][1]:
    se1, se2 = dic[pos]
    print(se1)
else: print("NONE")
'''
10 4
2 3 1 2 3 4 1 2 3 2
'''