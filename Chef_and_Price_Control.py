for i in range(int(input())):
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    lostrev = sum([i-k for i in p if i>k ])
    print(lostrev)