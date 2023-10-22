# for t in range (int(input())):
#     n = input()
#     if all (int(n[i]) <= int(n[i+1]) for i in range(0, len(n) - 1)):
#         print("YES")
#     else: print("NO")

#cach 2:
for t in range(int(input())):
    n = input()
    if n == "".join(sorted(n)): print("YES")
    else: print("NO")