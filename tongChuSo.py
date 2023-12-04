# n = input()
# res = 0
# while len(n) > 1:
#     n = str(sum((ord(i) - ord('0')) for i in n))
#     res += 1
# print(res)

n = int(input())
dem = 1
while True:
    n = sum(map(int, str(n)))
    if n < 10: break
    dem += 1
print(dem)