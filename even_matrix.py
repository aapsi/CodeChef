for t in range(int(input())):
    n = int(input())
    num = 0
    for i in range(n):
        if i%2 == 0:
            for j in range(n):
                num += 1
                print(num,end=' ')
            print()

        else:
            num = num + n+1
            for k in range(n):
                num -= 1
                print(num,end= ' ')
            num = num + n-1
            print()