up = 100000
prime = [True for i in range(up + 1)]
def sieve():
    prime[0], prime[1] = False, False
    i = 2
    while i*i <= up+1:
        if prime[i]:
            for j in range(i*i, up+1, i):
                prime[j] = False
        i += 1
        
sieve()
n, x = map(int, input().split())
cou, i = 0, 0
out = [x]
while cou < n:
    if prime[i]:
        out.append(i + out[-1])
        cou += 1
    i += 1
print(*out)
