for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    # dic = {}
    # for i in a:
    #     if dic.get(i) is None:
    #         dic.update({i:1})
    #     else : dic.update({i:dic.get(i) + 1})
    # for i in dic.items():
    #     if i[1] % 2 == 1:
    #         print(i[0])
    #         break
    for i in a:
        if a.count(i) % 2 == 1:
            print(i)
            break
        