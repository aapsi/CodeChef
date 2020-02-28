"""n = int(input())
#for n in range(1,1000):
i = 0
#for i in range (0,40,4):
if ( n in range(2**(2+i) ,2**(3+i)) for i in range (0,40,4)):
    d = 2
    print(d,end=",")
elif ( n in range(2**(3+i) ,2**(4+i))):
    d = 3
    print(d,end=",")
elif ( n in range(2**(4+i) ,2**(5+i))):
    d = 0
    print(d,end=",")
elif ( n in range(2**(5+i) ,2**(6+i))):
    d = 9
    print(d,end=",")
elif (n == 3) :
    d = 1
    print(d,end=",")
elif (n == 2):
    d = 1
    print(d,end=",")
elif (n == 1):
    d = 0
    print(d,end=",")"""

n = int(input())
for i, j in zip(range(4,10**18), range(8,10**18)):
    for n in range(i,j):
        if (i % 10 == 4 and j %10 == 8):
            d = 2
        if (i % 10 == 8 and j %10 == 6):
            d = 3
print(d)








0









