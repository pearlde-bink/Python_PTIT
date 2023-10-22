import itertools

n, k = [int(i) for i in input().split()]
se = {int(i) for i in input().split()}
for i in itertools.combinations(sorted(se), k):
    print(*i)

