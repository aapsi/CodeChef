for i in range(int (input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    adist = 0
    bdist = 0
    wd = 0
    for i in range(n):
        if adist == bdist and a[i] == b[i]:
            wd += a[i]
            adist += a[i]
            bdist += a[i]
        else:
            adist += a[i]
            bdist += b[i]
    print(wd)




