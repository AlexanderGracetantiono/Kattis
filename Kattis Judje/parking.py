a,b,c = map(int, input().split()) 
ta1,te1 = map(int, input().split()) 
ta2,te2= map(int, input().split()) 
ta3,te3= map(int, input().split()) 
total=0
truck=0
endall = max(te1,te2,te3)
for n in range(endall):
    if(n==ta1)|(n==ta2)|(n==ta3):
        truck+=1
    if(n==te1)|(n==te2)|(n==te3):
        truck-=1
    if(truck==1):
        total+=a
    elif(truck==2):
        total+=2*b
    elif(truck==3):
        total+=3*c
print(total)
