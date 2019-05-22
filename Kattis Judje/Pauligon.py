# this program is for open.kattis.com Pauleigon
# input is in one line rounds,paul,opp
# consideration:
# no draw, only score or not
# if its score below the change round, then round is in current player

ipt=str(input()).split()
rounds=int(ipt[0])
paul=int(ipt[1])
qoponent=int(ipt[2])
total =int( (paul+qoponent)/rounds)
total2= abs((total*rounds)-(paul+qoponent))
if(total2!=0)&(total2>rounds):
    total+=1
if(total%2==0):
    print("paul")
else:
    print("opponent")