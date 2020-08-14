for i in range(int (input())):
    pc, pr = map(int,input().split())
    a = pc//9
    b = pr//9
    c = pc%9
    d = pr%9
    if c != 0 and d != 0:
        dc = a+1
        dr = b+1
    if c == 0 and d == 0:
        dr = b
        dc = a
    if c!= 0 and d == 0:
        dc = a+1
        dr = b
    if c == 0 and d!= 0:
        dc = a
        dr = b+1
    if dc > dr:
        print(1, end = ' ')
        print(dr)
    if dr > dc:
        print(0, end = ' ')
        print(dc)
    if dr == dc:
        print(1,end=' ')
        print(dr)
