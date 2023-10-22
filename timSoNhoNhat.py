def smallest_number(string):
    min1 = 1000000
    number = ""
    for i in string:
        if i.isdigit():
            number += i
        else:
            if number != "":  # required cause int() cant convert empty string to number
                min1 = min(min1, int(number))
                number = ""
    # in case of the last index's value is a number, there's no value to compare to update min1 value
    if number != "":
        min1 = min(min1, int(number))
    return min1


t = int(input())

for _ in range(t):
    x = input().strip()
    minNum = smallest_number(x)
    print(minNum)
