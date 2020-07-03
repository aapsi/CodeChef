for i in range(int(input())):
    n = int(input())
    string = list(map(int,input().split()))
    x = [abs(t-s)-1 for s,t in zip(string,string[1:])]
    print(sum(x))