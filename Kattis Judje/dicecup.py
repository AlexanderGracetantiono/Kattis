xx= input().split(' ')
if (int(xx[0])>int(xx[1])):
    for n in range(int(xx[1]),int(xx[0])+1):
        print(n+1)
else:
    for n in range(int(xx[0]),int(xx[1])+1):
        print(n+1)
