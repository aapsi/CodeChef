for i in range(int(input())):
    rl = input()
    count = 0
    t = len(rl)
    if t == 2:
        if rl == 'xy' or rl == 'yx':
            count =1
        else:
            count = 0
    elif t == 1:
        count = 0
    else:
        j = 0
        while(j<t-1):
            if rl[j] == 'y' and rl[j+1] == 'x':
                j+=2
                count+=1
            elif rl[j] == 'x' and rl[j+1] == 'y':
                j+=2
                count+=1
            else:
                j+=1
    print(count)