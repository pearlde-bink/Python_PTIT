# dic1 = {1:'lan', 2:'hoa', 1:'lan'}
#return no duplicate dic
#c1
# for i in dic1:
#     count = 0
#     for y in dic1:
#         if i == y : count += 1
#     if count > 1: dic1.pop(i)
# print(dic1)
#c2
# setDic = {item for item in dic1.items()}
# print(setDic)

#count occurency of an element
word = ['red', 'green', 'red', 'blue', 'green', 'red'] 
dic = {}
for i in range (0, len(word) - 1):
    count = 0
    j = i + 1
    while j < len(word):
        if(word[i] == word[j]):
            count += 1
            word.remove(word[j])
        j += 1
    dic[i] = count
print(dic)
