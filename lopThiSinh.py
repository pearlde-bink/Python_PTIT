class ts:
    def __init__(self, ten, dob, d1, d2, d3):
        self.ten = ten
        self.dob = dob
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.to = d1 + d2 + d3
    def prin(self):
        print(self.ten + " " + self.dob + " " + "{:.1f}".format(self.to))
        
        
s = input()
s2 = input()
d1 = float(input())  
d2 = float(input())   
d3 = float(input())  

t = ts(s, s2, d1, d2, d3)  
t.prin()
    