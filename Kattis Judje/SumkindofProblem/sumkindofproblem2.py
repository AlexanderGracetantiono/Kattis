cases= int(input())
for n in range(cases):
    x,y=map(int,input().split())
    p2=y*y
    print(x,int((p2+y)/2),p2,p2+y)