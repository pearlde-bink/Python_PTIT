for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    left, right = [0] * n, [0] * n
    left[0], right[-1] = a[0], a[-1]
    for i in range(1, n):
        left[i] = max(left[i-1], a[i])
    for i in range(n - 2, -1, -1):
        right[i] = min(right[i+1], a[i])
    val = len([a[i] for i in range(1, n-1) if left[i-1] <= a[i] and right[i+1] > a[i]])    
    if a[0] < right[1]: val += 1
    if a[-1] >= left[-2]: val += 1
    print(val)
        