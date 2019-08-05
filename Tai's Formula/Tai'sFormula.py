iterl = int(input())
arrvol = []*(0)
arrmol =[]*(0)
for i in range(iterl):
    ipt = str(input()).split()
    arrmol.append(float(ipt[1]))
    arrvol.append(float(ipt[0]))

res =0
for n in range(1, len(arrmol)):
    res += (((float(arrmol[n]) + float(arrmol[n - 1])) / 2) * (float(arrvol[n]) - float(arrvol[n - 1]) ))
    
print(res/1000)