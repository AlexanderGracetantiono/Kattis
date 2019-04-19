while True:
    x,y=map(int,input().split())
    if(x==0)&(y==0):
        break
    kon=int(x/y)
    sisa=(x-(kon*y))
    print(kon,sisa,"/",y)