import math
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    m=[]
    while True:
        x=[int(i) for i in input().split()]
        m+=x
        if (len(m)==a):
            break
    val = 100000
    for i in range(len(m)):
        if m[i] % b == 0:
            tmp = m[i]
            for j in range(i, len(m)):
                tmp = math.gcd(tmp, m[j])
                if tmp < b:
                    break
                elif tmp == b:
                    val = min(val, j-i+1)
                    break
    print(val if val != 100000 else -1)

"""
3
8 3
6 9 7 10 12 24 36 27
4 3
2 4 6 8
4 6
1 2 3 6
 """      
