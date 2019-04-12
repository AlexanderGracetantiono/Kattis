def sumstr(xxx):
    temp=0
    for x in xxx:
            temp+=ord(x)-48
    return temp

cases=int(input())
for i in range(cases):
    sumipt=0
    oript=str(input())
    # listor example 30 or 198
    sumipt=sumstr(oript)
    for n in range(int(oript),-1,-1):
        if(sumstr(str(n)))<sumipt:
            print(n)
            break