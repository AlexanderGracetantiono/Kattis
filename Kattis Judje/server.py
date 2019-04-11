datas=str(input()).split()
times=str(input()).split()
t=int(datas[1])
task=0
for x in times:
    t-=int(x)
    if(t<0):
        break
    else:
        task+=1
print(task)