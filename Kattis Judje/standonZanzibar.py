cases=int(input())
for e in range(cases):
    ipt=str(input()).split()
    x=0
    totalimpt=0
    for num in ipt:
        if((x==0)&(int(num)>0)):
            x=int(num)
        elif(int(num)==0):
            break
        elif(int(num)>(x*2)):
            totalimpt+=(int(num)-(x*2))
        x=int(num)
    print(totalimpt)