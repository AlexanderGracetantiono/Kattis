cases=0
while True:
    cases+=1
    n=int(input())
    if n<=0:
        break
    store=[0]*(n)
    storenum=[0]*(n)
    for nn in range(0,n):
        xx=input().split(' ')
        store[nn]=xx[len(xx)-1].lower()
        storenum[nn]=1
    store.sort()
    print("List ",cases,":",sep="")
    for nnn in range(n):
        for ninn in range(nnn+1,n):
            if(store[nnn]!="false"):
                if(store[nnn]==store[ninn]):
                    store[ninn]="false"
                    storenum[nnn]+=1
        if(store[nnn]!="false"):
            print(store[nnn],"|",storenum[nnn])
        
