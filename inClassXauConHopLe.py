# #doc tu tep A, tim xau con dai nhat hop le: moi dong chua ki tu dong mo ngoac () dung

def isValid(s):
    stack = []
    ind = 0
    doDai = 0
    maxLength = 0
    for i in range(0, len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if stack:
                start = stack.pop()
                doDai = i - start + 1
                if doDai > maxLength: 
                    maxLength = doDai
                    ind = start
            else: 
                doDai = 0  
    if maxLength > 0:
        print(s[ind : ind + maxLength])  
        
with open('B.txt') as f:
    for x in f:
        isValid(x)
      
