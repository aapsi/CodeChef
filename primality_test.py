for _ in range(int(input())):
    n = int(input())
    c=0
    for i in range(2,n//2):
        if (n%i==0):
            c=1
            break
    if c==1:
        print("no")
    else:
        print("yes")