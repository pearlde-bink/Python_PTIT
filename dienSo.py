'''for t in range(int(input())):
    n = int(input())
    a = {int(i) for i in input().split()}
    print(max(a) - min(a) + 1 - len(a))'''
    
for _ in range(int(input())):
    n = int(input())
    li = [int(i) for i in input().split()]
    dem = 0
    li.sort()
    for i in range(len(li) - 1):
        for j in range(i+1, len(li)):
            if li[j] - li[i] > 1: 
                dem += li[j] - li[i] - 1
                break
            else: break
    print(dem)
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    