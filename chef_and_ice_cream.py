for i in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    c5 = 0
    c10 = 0
    c15 = 0
    flag = 0
    for j in range(n):
        if p[j] == 5:
            c5+=5
        elif p[j] == 10 and c5>0:
            c10+=10
            c5-=5
        elif p[j] == 15 and c10>=10:
            #c15+=15
            c10-=10
        elif p[j] == 15 and c5>=10:
            #c15+=15
            c5-=10
        else:
            flag = 1
            break
    if flag == 1:
        print('NO')
    else:
        print('YES')



