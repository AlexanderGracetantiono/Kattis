x=str(input()).split()
sum1=int(x[1])-int(x[0])
sum2=int(x[2])-int(x[1])
sum1-=1
sum2-=1
if(sum1>sum2):
    print(sum1)
else:
    print(sum2)