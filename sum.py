t = int(input())
l1 = []
l2 = []
l3 = []
for _ in  range(t):
   orig = [1,2,3]
   sum = 0
   l = list(map(int,input().split()))
   for i in l:
       sum += i
   t2 = sum/2
   a = l.count(orig[0])
   b = l.count(orig[1])
   c = l.count(orig[2])
   l1 = l[:a]
   l2 = l[a:a+b]
   l3 = l[(a+b):]
   print(l1)
   print(l2)
   print(l3)
   while t2 >0:
       for





