x="input"
while x!="0 0":
    x=input().split()
    #print(x)
    h=int(x[0])
    t=int(x[1])
    if ((h==0) & (t==0)):
            break
    #print(h,t)
    iterasi=0
    while True:
        #example
        #3 3, 4 1, 2 1, 0 1,0 2,03, 04,12,20,00
        #f,
        #print(h,t,iterasi)
        if ((h==0) & (t==0)):
            break
        if t>=2 :
            t-=2
            h+=1
        elif h>=2:
            h-=2
        else:
            t+=1
        iterasi+=1
    print(iterasi)
    
