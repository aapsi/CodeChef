for i in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    min = max(l)
    ele = 0
    flag = 0
    flag2 = 0
    for j in range(len(l)):
        if l[j] == k:
            print(l[j])
            flag = 1
            break
        if l[j] > k:
            pass
        if k % l[j] == 0:
            if k//l[j]-1 < min:
                min = k//l[j]-1
                ele = l[j]
                flag2 =1
    if flag2 == 1 and flag ==0:
        print(ele)
    elif flag == 0 and flag2 ==0:
        print(-1)
