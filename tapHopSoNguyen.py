n, m = [int(i) for i in input().split()]
a = {int(i) for i in input().split()}
b = {int(i) for i in input().split()}
print(*sorted(a&b))
print(*sorted(a-b))
print(*sorted(b-a))