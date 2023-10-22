"""for t in range(int(input())):
    p, q = input().split()
    x1 = input()
    a = list(x1)
    x2 = input()
    b = list(x2)

    for i in range(len(a)):
        if a[i] == str(q):
            a[i] = str(p)  # convert to minimum
    for i in range(len(b)):
        if b[i] == str(q):
            b[i] = str(p)  # convert to minimum
    x1 = "".join(a)
    x2 = "".join(b)
    sumMin = int(x1) + int(x2)

    for i in range(len(a)):
        if a[i] == str(p):
            a[i] = str(q)  # convert to maximum
    for i in range(len(b)):
        if b[i] == str(p):
            b[i] = str(q)  # convert to maximum
    x1 = "".join(a)
    x2 = "".join(b)
    sumMax = int(x1) + int(x2)

    if sumMin > sumMax:
        print(sumMax, end=" ")
        print(sumMin)
    else:
        print(sumMin, end=" ")
        print(sumMax)"""

for t in range(int(input())):
    p, q = input().split()
    arr = input().split()
    if len(arr) == 1:
        x1 = arr[0]
        x2 = input()
    else:
        x1, x2 = arr
    sumMax = int(x1.replace(min(p, q), max(p, q))) + int(
        x2.replace(min(p, q), max(p, q))
    )
    sumMin = int(x1.replace(max(p, q), min(p, q))) + int(
        x2.replace(max(p, q), min(p, q))
    )

    print(sumMin, sumMax)
