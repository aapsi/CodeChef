for i in range(int(input())):
    h,p = map(int,input().split())
    if p >= h/2:
        print(1)
    else:
        print(0)