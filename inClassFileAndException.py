with open('A.txt') as c1:
    arr = c1.readlines()
        
with open('B.txt') as c2:
    brr = c2.readlines()

for i in arr:
    for y in brr:
        try:
            print(int(i) * int(y))
            break
        except ValueError:
            print("skip")
            break

            