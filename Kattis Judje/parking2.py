# this code if for kattis.com
# the first input is cases 
# next input process how many shop person want to go
# next input is in what km is the shop,( consider the road is just straight
# ex: 2 11 5 99 3 2)
# output will be how long it takes from parking to first shop and the near shop.. etc
# consideration:
#     1. person is parking on the last km shop so in the end it comes back to his car
#     2. person is strong so it can walk 30km 
#     3.person dont want to pay park twice or more... he is economist

cases=int(input())
while(cases>0):
    cases-=1
    numstore=int(input())-1
    longstore=str(input()).split()
    longstore = list(map(int, longstore))
    temp=int(longstore[numstore])
    longstore.sort()
    lastnum=temp
    total=0
    for n in range(len(longstore)):
        if(longstore[n]!=temp):
            total+=abs(lastnum-int(longstore[n]))
            lastnum=int(longstore[n])

    total+=abs(lastnum-temp)
    print(total)