import math

ipt = str(input()).split()
res = 0
s = 0

for i in range(4):
    s += int(ipt[i])
s/=2
res = (s - int(ipt[0])) * (s - int(ipt[1])) * (s - int(ipt[2])) * (s - int(ipt[3]))
res =math.sqrt(res)
print(res)