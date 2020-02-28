(x,y)=map(float,input().split())
if x>0 and x<=2000 and y>=0 and y<=2000 and (x+0.50<=y) and (x%5==0):
    print('%.2f'%(y-x-0.50))
else:
    print('%.2f'%y)

