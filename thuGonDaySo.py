"""n = int(input())

list1 = []

for i in range(n):
    list1.append(int(input()))

i = 0
while i < len(list1) - 1:
    if (list1[i] + list1[i + 1]) % 2 == 0:
        list1.remove(list1[i])
        list1.remove(list1[i])
    else:
        i += 1

print(len(list1))"""

"""n = int(input())
list = [int(i) for i in input().split()]
i = 1
while i < len(list):
    if (list[i-1]+list[i]) % 2 == 0:
        list.pop(i)
        list.pop(i-1)
        if i > 1:
            i -= 1
    else:
        i += 1
print(len(list))"""


def shortenList(A):
    Acopy = A.copy()
    i = 0
    while i < len(Acopy) - 1:
        if (Acopy[i] + Acopy[i + 1]) % 2 == 0:
            Acopy.pop(i)
            Acopy.pop(i)
            if i > 0:
                i -= 1
        else:
            i += 1
    return len(Acopy)


n = int(input())
list1 = [int(x) for x in input().split()]

result = shortenList(list1)

print(result)
