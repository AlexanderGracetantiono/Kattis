cases=int(input())
while cases!=0:
    paths=str(input()).split()
    x=60/float(paths[1])
    xx=x*float(paths[0])
    print(xx-x,xx,xx+x)
    cases-=1