a = []
while len(a) < 10:
    a.extend(input().split())

se = set(int(i) % 42 for i in a)
print(len(se))

