for i in range(int(input())):
    a = list(map(int,input().split()))
    p = a[-1]
    arr = a[0:5]*p
    asum = sum(arr)
    if(asum>120):
        print("Yes")
    else:
        print("No")