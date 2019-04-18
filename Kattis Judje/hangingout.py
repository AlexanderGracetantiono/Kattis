x=str(input()).split()
maxpeople=int(x[0])
curr=0
itelation=int(x[1])
canselgrp=0
for i in range(itelation):
    ipt= str(input()).split()
    if(ipt[0]=="enter"):
        if(curr+int(ipt[1]))>maxpeople:
            canselgrp+=1
        else:
            curr+=int(ipt[1])
    elif(ipt[0]=="leave"):
        curr-=int(ipt[1])
print(canselgrp)