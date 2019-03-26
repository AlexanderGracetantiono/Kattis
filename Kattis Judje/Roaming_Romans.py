x=float((5280/4854)*1000)
c=float(input())
cx=x*c
if((int(cx)+0.5)<cx):
    print(int(cx+1))
else:
    print(int(cx))
