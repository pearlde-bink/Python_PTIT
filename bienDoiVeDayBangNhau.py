def step(a, b):
    return abs(a - b)

n = int(input())
a = [int(i) for i in input().split()]
dict = {}
for i in a:
    steps = 0
    for j in a:
        steps += step(i, j)
    dict.update({i: steps})
sDict = sorted(dict.items(), key = lambda x : x[1]) #sort with value, then sDict is list of tuples
x, y = next(iter(sDict)) #get 1st item
print(f'{y} {x}')
