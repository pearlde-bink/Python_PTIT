#sort tuple in list using lambda          
# a = [('English', 88), ('Science', 90), ('Math', 82)]
# a.sort(key = lambda tup: tup[1])
# print(a)


#viet ham tinh giai thua cua 1 so tu nhien, va dat trong 1 module
# def gt(n):
#     val = 1
#     for i in range(2, n+1):
#         val *= i
#     return val

#ham doc va hien thi du lieu trong file csv
#c1
# def readAndShow():    
#     # try:
#     with open("addresses.csv") as f:
#         for x in f:
#             s = x.split(',')
#             print(s[len(s) - 2])
#     # except FileNotFoundError:
#     #     print("File not found.")
# readAndShow()   
#c2
import csv
f = open('addresses', 'r')
cc = csv.reader(f)
for i in cc:
    print(i[4])
        
        
