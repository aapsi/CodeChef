t = int(input())
for i in range(t):
    n = int(input())
    f0 = 0
    f1 = 1
    D =[]

    if n>2:
        F = [0, 1]
        for _ in range(n -2):
            temp = f0 + f1
            f0 = f1
            f1 = temp
            F.append(temp)
    elif n == 2:
        F = [0,1]

    elif n == 1:
        F = [0]


    D = F[:]

    for i in range(len(D)):
        D[i] = D[i] % 10

    while len(D) > 1:
        D = D[1::2]

    print(D)








