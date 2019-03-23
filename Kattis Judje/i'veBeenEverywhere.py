cases=int(input())
for n in range(cases):
    casescase=int(input())
    listdata=[""]*(casescase)
    for nn in range(casescase):
        listdata[nn]=str(input())
    for nn in range(casescase):
        for nnn in range(casescase):
            if((listdata[nn]==listdata[nnn])&(nn!=nnn)):
                listdata[nnn]="false"
    ntotal=0
    for nn in range(casescase):
        if(listdata[nn]!="false"):
            ntotal+=1
    print(ntotal)