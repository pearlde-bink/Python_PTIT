base = "0123456789ABCDEF"
with open('DATA.in') as f:
    t = int(f.readline())
    for _ in range(t):
        b = int(f.readline())
        x = int(f.readline(), 2) #convert to decimal
        ans = ""
        while x:
            ans += base[x%b]
            x //= b
        print(ans[::-1])
        
    
    