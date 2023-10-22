for t in range (int(input())):
    n = input() 
    a = list(n) #convert to list
    outcome = ""
    for i in range(0, len(a)):
        if a[i] == "-1": continue
        count = 1
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                count += 1
                a[j] = "-1"
            else: break
        outcome += str(count)
        outcome += str(a[i])

    print(outcome)