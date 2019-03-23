n=int(input())
xx=sorted([int(x) for x in input().split()])
val=1
bools=True
for i in range(1, n+1):
    if xx[i-1] >i:
        bools=False
        break
    val=min(val,xx[i-1]/(i))
if bools:
    print(val)
else:
    print('impossible')
