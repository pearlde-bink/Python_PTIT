for t in range(int(input())):
    n = int(input())
    list1 = sorted([int(x) for x in input().split()])
    count = 0
    for i in range(0, n-2):
        left = i + 1
        right = n - 1
        while left < right:
            sum = list1[i] + list1[left] + list1[right]
            if sum == 0: 
                count += 1
                left += 1
            elif sum < 0 :
                left +=1
            else: right -=1
            
    print(count)
    
