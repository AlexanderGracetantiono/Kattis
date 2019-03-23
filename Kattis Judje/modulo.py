maxs=0
listx=["False"]*(10)
for n in range(10):
#    print(listx)
#modulo is a program taht count how many x can be modulo by 42
#input is int x, do it for 10 iteration
    x=int(input())
    for nnn in range(0,n+1):
        if(x%42!=listx[nnn]):
            if(listx[nnn]=="False"):
                listx[nnn]=x%42
                maxs+=1
                break
        else:
            break

print(maxs)