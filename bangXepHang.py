import functools
class Submit:
    def __init__(self, name, correct, sub):
        self.name = name
        self.correct = correct
        self.sub = sub
    
def cmp(s1, s2):
    if s1.correct < s2.correct: return 1
    elif s1.correct > s2.correct: return -1
    else:
        if s1.sub < s2.sub: return -1
        elif s1.sub > s2.sub: return 1
        else:
            if s1.name > s2.name : return 1
            else: return -1
                
                
a = []
for _ in range(int(input())):
    s = input()
    m, n = [int(x) for x in input().split()]
    a.append(Submit(s, m, n))
    
a = sorted(a, key = functools.cmp_to_key(cmp))
for i in a:
    print(i.name, i.correct, i.sub)
"""
2
Nguyen Van Nam
168 600
Tran Thi Ngoc
168 600
    """   
