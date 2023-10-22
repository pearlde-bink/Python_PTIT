for t in range (int(input())):
    n = int(input())
    li = [int(x) for x in (input().split())]
    
    minSum = 0
    x = 3
    while x > 0 and li:
        minNum = min(li)
        li.remove(minNum)
        minSum += minNum
        x -= 1
    print(minSum)
    
    