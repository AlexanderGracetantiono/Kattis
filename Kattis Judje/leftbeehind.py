while(True):
    ipt=str(input()).split()
    gd=int(ipt[0])
    sr=int(ipt[1])
    if((gd==0)&(sr==0)):
        break
    elif((gd+sr)==13):
        print("Never speak again.")
    elif(gd>sr):
        print("To the convention.")
    elif(gd<sr):
        print("Left beehind.")
    else:
        print("Undecided.")
