cases=int(input())
for i in range(cases):
    oript=0
    sumipt=0
    oript=str(input())
    # listor example 30 or 198
    for x in oript:
        sumipt+=ord(x)-48
    for n in range(int(oript),-1,-1):
        tempsum=0
        for xx in str(n):
            tempsum+=ord(xx)-48
        if(tempsum==(sumipt-1)):
            sumipt=int(n)
            break
    print(sumipt)