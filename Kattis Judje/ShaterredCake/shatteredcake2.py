import sys
wcake=int(input())
temp=int(input())
total=0
for x in range(temp):
    xx=sys.stdin.readline().split()
    total+=(int(xx[0])*int(xx[1]))
sys.stdout.write(str(int(total/wcake)))