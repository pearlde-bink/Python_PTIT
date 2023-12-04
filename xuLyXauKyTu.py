s1 = set((i for i in input().lower().split()))
s2 = set((i for i in input().lower().split()))
hop = s2
giao = set(())
for i in s1:
    if i in s2: giao.add(i)
    else: hop.add(i)
    
giao = sorted(giao)
hop = sorted(hop)
for i in hop:
    print(i, end = " ")
print()
for i in giao: 
    print(i, end = " ")
print()

# s1 = {i for i in input().lower().split()}
# s2 = {i for i in input().lower().split()}

# print(*sorted(s1|s2))
# print(*sorted(s1&s2))