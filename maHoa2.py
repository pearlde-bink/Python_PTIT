p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    checkZero = input() #input k and s
    if checkZero == '0': #check if input is '0' then stop program
        break
    k, s= checkZero.split() #split input
    k = int(k)
    
    encode = ""
    for i in s:
        encode += p[(p.find(i) + k) % 28]

    reversedString = encode[::-1]

    print(reversedString)

