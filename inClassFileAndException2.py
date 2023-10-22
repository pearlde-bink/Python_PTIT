#my mother is a person i admire most. she devoted a lot of time and energy to the upbringing of my two brothers and 1. despite working hard, she always made time to teach us many useful things which are necessary and important in our later lives. moreover, she is a good role model for me to follow. she always tries to get on well with people who live next door and help everyone when they are in difficulties, so most of them respect and love her. i admire and look up to my mother because she not only brings me up well but also stands by me and gives some help if necessary. for example, when i encounter some difficulties, she will give me some
#tim nhung tu dai nhat trong doan van tren

with open('A.txt') as f:
    s = f.read()
a = list(s.split())
a = list(set(a))
m = 0
for i in a: 
    if len(i) > m: m = len(i)
for i in a:
    if len(i) == m:
        print(i)        
