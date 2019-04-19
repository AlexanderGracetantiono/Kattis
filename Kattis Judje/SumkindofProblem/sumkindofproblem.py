cases=int(input())
for i in range(cases):
    n,m=map(int, input().split())
    pos=0
    odd=0
    even=0
    mark1=0
    mark2=0
    for s in range(1,10000):
        if(s<=m):
            pos+=s
        if((s%2!=0)&(mark1<=m)):
            odd+=s
            mark1+=1
        elif((s%2==0)&(mark2<=m)):
            even+=s
            mark2+=1
        if((mark1>=m)&(mark2>=m)):
            break
    print(n,pos,odd,even)
    