def sumDigits(no):
    return 0 if no == 0 else int(no%10) + sumDigits(int(no/10))
for i in range(int(input())):
    n = int(input())
    c = 0
    m = 0
    win = 0
    for j in range(n):
        a,b = map(int,input().split())
        sa = sumDigits(a)
        sb = sumDigits(b)
        if sa>sb:
            c += 1
        elif sb> sa:
            m += 1
        else:
            c+=1
            m+=1
    if c > m:
        win = 0
        print(win,c)
    elif m > c :
        win = 1
        print(win,m)
    else:
        win = 2
        print(win,c)