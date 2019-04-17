cases=int(input())
data=str(input()).split()
min=1000000
day=0
for n in range(len(data)):
    if(int(data[n])<min):
        min= int(data[n])
        day=n
print(day)
