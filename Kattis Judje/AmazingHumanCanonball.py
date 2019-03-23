def time(v,o,x1):
    return x1/(v*math.cos(o*math.pi/180.00))
def ypo(v,t,o):
    return v*t*math.sin(o*math.pi/180.0)- (0.5 * 9.81 *t*t)

import math
cases=int(input())
for x in range(cases):
    varx=str(input()).split()
    v=float(varx[0])
    o=float(varx[1])
    x1=float(varx[2])
    h1=float(varx[3])
    h2=float(varx[4])
    t=time(v,o,x1)
    yposfix=float(ypo(v,t,o))
    if(h1+1<yposfix)&(yposfix<h2-1):
        print("Safe")
    else:
        print("Not Safe")

