def biggest_num(string):
    max1 = 0
    number = 0
    for i in string:
        if i.isdigit():
            number = number * 10 + int(i)
        else:
            if number != 0:
                max1 = max(max1, number)
                number = 0
    # in case of the last index's value is a number, there's no value to compare to update max1 value
    if number != 0:
        max1 = max(max1, number)
    return max1


t = int(input())
for _ in range(t):
    x = input().strip()
    maxNum = biggest_num(x)
    print(maxNum)
