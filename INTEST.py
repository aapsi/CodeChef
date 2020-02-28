n = int(input())
a = 0
b = 0
l = 0
w = 0
for _ in range(n):
    (s,t) = map(int,input().split())
    a += s
    b += t
    diff = abs(a - b)
    if diff>0:
        l = diff
        if a>b:
            w = 1
        else:
            w = 2
print(w, end=" ")
print(l)



