Var_Cases = int(input())
for i in range(Var_Cases):
    Var_Days = input().split(" ")
    Candle = ((int(Var_Days[1])/2)*(int(Var_Days[1])+1))+int(Var_Days[1])
    print(Var_Days[0],int(Candle))