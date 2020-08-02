def GetVolume(Var_H,Var_V):
    return Var_V*Var_H*4

Var_Length_Horizontal_vertical=input()
Arr_Lenght = Var_Length_Horizontal_vertical.split(" ")
Var_Lenght =  int(Arr_Lenght[0])
Arr_H = []
Arr_V = []

Var_Horizontal = int(Arr_Lenght[1])
Var_Vertical =  int(Arr_Lenght[2])
Arr_H.append(Var_Horizontal)
Arr_V.append(Var_Vertical)
Arr_H.append(Var_Lenght-Var_Horizontal)
Arr_V.append(Var_Lenght-Var_Vertical)
Var_Max_Volume = 0

for i in range(len(Arr_H)):
    for j in range(len(Arr_V)):
        Var_Volume = GetVolume(Arr_H[j],Arr_V[i])
        # print("H,V,VOL :",Arr_H[j],Arr_V[i],Var_Volume)
        if(Var_Volume>Var_Max_Volume):
            Var_Max_Volume = Var_Volume

print(Var_Max_Volume)
