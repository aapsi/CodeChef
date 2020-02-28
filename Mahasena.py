T = int(input())
count=0
val = list(map(int, input().split()))
for i in range(T):
    count = count-1 if val[i]%2==1 else count+1
retval = "READY FOR BATTLE" if count>0 else "NOT READY"
print(retval)