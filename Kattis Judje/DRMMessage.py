def atonum(x):
    cs=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    #print(len(cs))//26
    for c in range(len(cs)):
        if(x==cs[c]):
            return c
def numtoa(num):
    cs=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for c in range(len(cs)):
        if(num%26==c):
            #print(num)
            return cs[num%26]
        
def rotate(kalimat):
    tnum=0
    num=[0]*(len(kalimat))
    for x in range(0,len(kalimat)):
        temp1=kalimat[x]
        num[x]=atonum(temp1)
        tnum+=num[x]
    temp2=""
    for xx in range(0,len(kalimat)):
        temp2+=numtoa(int(num[xx]+tnum))
    return temp2

def merges(kal1,kal2):
    temp3=""
    for x in range(len(kal1)):
        temp1=atonum(kal1[x])
        temp2=atonum(kal2[x])
        temp3+=numtoa(temp2+temp1)
    return temp3

kal=str(input())
kal1=kal[0:int(len(kal)/2)]
kal2=kal[int(len(kal)/2):int(len(kal))]
kal1=rotate(kal1)
kal2=rotate(kal2)
print(merges(kal1,kal2))