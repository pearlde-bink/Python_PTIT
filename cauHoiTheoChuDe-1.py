n = int(input())
a = []
s = ''
for i in range(n) :
    s = input()
    a.append(s)
    if s == '' :
        n += 1
        print(a[0] + ':', len(a) - 2)
        a.clear()
print(a[0] + ':', len(a) - 1)
"""
9
Home/accommodation
What kind of housing/accommodation do you live in?
Who do you live with?
How long have you lived there?

Study
Describe your education
What is your area of specialization?
Why did you choose to study that major?
"""    
