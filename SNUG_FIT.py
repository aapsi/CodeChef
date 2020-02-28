t = int(input())
for i in range(t):
    s = 0
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if len(set(a))==1 and len(set(b)) == 1:
        print(min(a[0],b[0])*n)
    else:
        a.sort(reverse = True)
        b.sort(reverse = True)
        for i in range(n):
            d = min(a[i],b[i])
            s+=d
        print(s)




