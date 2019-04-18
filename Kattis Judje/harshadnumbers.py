def additic(x):
    sum=0
    for n in str(x):
        sum+=int(n)
    return float(float(x)/sum)

x= int(input())
check=0.0
checknt=0
while True:
    check=additic(x)
    checknt=int(check)
    if(check==checknt):
        print(x)
        break
    else:
        x+=1

