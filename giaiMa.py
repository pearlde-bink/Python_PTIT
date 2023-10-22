for t in range (int(input())):
    n = input()
    outcome = n[0]
    for i in range(1, len(n)):
        if n[i] >= 'A' and n[i]<= 'Z': outcome += n[i]
        elif int(n[i]) <= 9 and int(n[i]) > 0:
            for j in range (0, int(n[i]) - 1): outcome += n[i-1]
    
    print(outcome)