hand=str(input()).split()
tcard=[""]*(5)
counter=[1]*(5)
for n in range(len(hand)):
    temp=hand[n][0]
    tcard[n]=temp
for n in range(len(tcard)-1):
    for m in range(n+1,len(tcard)):
        if((tcard[n]==tcard[m])&(tcard[m]!="")):
            tcard[m]=""
            counter[n]+=1
max=0
for n in range(len(counter)):
    if(counter[n]>max):
        max=counter[n]
print(max)

        