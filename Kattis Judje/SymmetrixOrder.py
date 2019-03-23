lp=1
while True:
    x=int(input())
    if(x==0):
        break
    listdata=[""]*(x)
    datalen=[0]*(x)
    frs=0
    las=x-1
    for n in range(1,x+1):
        if(n%2==0):
            listdata[las]=str(input())
            las-=1
        else:
            listdata[frs]=str(input())
            frs+=1
    print("SET",lp)
    for n in range(x):
        print(listdata[n])
    lp+=1