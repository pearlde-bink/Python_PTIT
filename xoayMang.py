for _ in range(int(input())):
    n, d= map(int, input().split())
    list = input().split()
    print(*(list[d:] + list[:d])) # * is used to unpack each elements of list[d:] + list[:d]