wcake=int(input())
pieces=int(input())
total=0
for x in range(pieces):
    xxx=str(input()).split()
    total+=(int(xxx[0])*int(xxx[1]))
print(int(total/wcake))