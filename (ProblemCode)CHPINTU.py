t = int(input())
for i in range(t):
    n,m= map(int,input().split())
    F = list(map(int,input().split()))
    P = list(map(int,input().split()))
    setlist =list(set(F))
    typedict = [0]*(len(setlist))
    for j in range(len(setlist)):
        for k in range(n):
            if setlist[j] == F[k]:
                typedict[j]+=P[k]
    new_list = [item for item in typedict if item != 0]
    print(min(new_list))

