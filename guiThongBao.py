'''for t in range(int(input())):
    list = [i for i in input().split()]
    count = 0
    for i in list:
        if count + len(i) > 100:    break
        print(i, end='')
        count += len(i)
        print(end=' ')
        count += 1
    print()'''
    
for _ in range(int(input())):
    tb = input()   
    if len(tb) < 100: 
        print(tb)
        continue
    if tb[100] == " ":
        print(tb[:100])
    else:
        for i in range(100, 90, -1):
            if tb[i] == " ":
                index = i
                break
        print(tb[:index])

'''
2
Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va hoc ky phu ky he nam hoc 2020 – 2021
Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    