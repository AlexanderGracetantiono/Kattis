# this program is for open.katttis.com Volim problem
# first input is curr player that have the 'bomb'
# next input is sum of question,
# next input consist of time and answer is (T)rue of anything else
# True answer pass the bomb to another player
# else answer is still be counted (time) but player is same
#  output is which player have the bomb if the time is >=210 second
# consideration:
# player is 8, no more no less no change
# answer can be True No or skiP

currplayer=int(input())
question=int(input())
time=0
game='ON'
for i in range(question):
    ipt=str(input()).split()
    if(game=='ON'):
        if(ipt[1]=='T'):
            time+=int(ipt[0])
            if(time<210):
                if(currplayer==8):
                    currplayer=1
                    # limit player
                elif(currplayer<8):
                    currplayer+=1
                    # give to another player
            else:
                game='OFF'
                # time exceded limit
        else:
            time+=int(ipt[0])
            # answer is fasle or skip
print(currplayer)