def isValid(s):
    a = s.count('A')
    b = s.count('B')
    c = s.count('C')
    oke = False
    if (a > 0 and b > 0 and c > 0) and len(s) >= 3 and (a <= b and b <= c):
       oke = True
    return oke
 
def backtrack(i, s, n, list):
       if i > n: return 
       if isValid(s): list += [s]
       if i < n:
           backtrack(i+1, s + 'A', n, list)
           backtrack(i+1, s + 'B', n, list)
           backtrack(i+1, s + 'C', n, list)
           
list = []
backtrack(0, '', int(input()), list)
list.sort(key = lambda k: (len(k), k))
print(*list, sep = '\n')           