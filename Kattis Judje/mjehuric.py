# simpleSOrt
ipt=str(input()).split()
ipt = list(map(int, ipt))
swap='no'
for n in range (len(ipt)):
    for i in range (1,len(ipt)):
        swap='no'
        if(swap=='no'):
            if(ipt[i]<ipt[i-1]):
                temp=ipt[i-1]
                ipt[i-1]=ipt[i]
                ipt[i]=temp
                swap='yes'
                print(ipt[0],ipt[1],ipt[2],ipt[3],ipt[4],)
                
