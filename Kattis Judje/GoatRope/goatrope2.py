import math
kal=str(input()).split()
x=float(kal[0])
y=float(kal[1])
x1=float(kal[2])
y1=float(kal[3])
x2=float(kal[4])
y2=float(kal[5])
r=0.0
if((x>x1)&(x<x2)&(y>y2)):
    r=(float(y))-(float(y2))

elif((x>x2)&(y>y2)):
    r=math.hypot(x-x2,y-y2)

elif((x>x2)&(y>y1)&(y<y2)):
    r=(float(x))-(float(x2))

elif((x>x2)&(y<y1)):
    r=math.hypot(x-x2,y1-y)

elif((x>x1)&(x<x2)&(y<y1)):
    r=(float(y1))-(float(y))
    
elif((x<x1)&(y<y1)):
    r=math.hypot(x1-x,y1-y)

elif((x<x1)&(y>y1)&(y<y2)):
    r=(float(x1))-(float(x))

elif((x<x1)&(y>y2)):
    r=math.hypot(x1-x,y-y2)
   
print(r)