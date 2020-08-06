Var_Cases = int(input())
Arr_Winner=[""]*12
for i in range(Var_Cases):
    Var_Code_Name = input()
    Var_Code_Name_split = Var_Code_Name.split(" ")
    for n in range(len(Arr_Winner)):
        if(Arr_Winner[n]==""):
            Arr_Winner[n]=Var_Code_Name
            break
        else:
            if(Arr_Winner[n].split(" ")[0]==Var_Code_Name_split[0]):
                break
for g in range(len(Arr_Winner)):
    print(Arr_Winner[g],end="\n")
