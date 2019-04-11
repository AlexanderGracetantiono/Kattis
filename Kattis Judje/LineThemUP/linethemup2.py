cases=int(input())
orlist=[""]*(cases)
stlist=[""]*(cases)
for i in range(cases):
    x=str(input())
    orlist[i]=x
    stlist[i]=x
stlist.sort()
if(stlist==orlist):
    print("INCREASING")
else:
    stlist.sort(reverse=True)
    if(stlist==orlist):
        print("DECREASING")
    else:
        print("NEITHER")
