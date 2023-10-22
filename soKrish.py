def giaiThua(n):
    gt = 1
    for i in range(2, n + 1):
        gt *= i
    return gt
        
for _ in range(int(input())):
    n = input()
    sum = 0
    for i in n:
        sum += giaiThua(int(i))
    print("Yes") if sum == int(n) else print("No")