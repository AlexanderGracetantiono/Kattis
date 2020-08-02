
Many_FBI=0
Arr_FBI = []
for i in range(5):
    Var_String_Ipt = input()
    for j in range(len(Var_String_Ipt)):
        # print("data: ",Var_String_Ipt[j])
        if(Var_String_Ipt[j] == "F"):
            if(Var_String_Ipt[j+1]=="B"):
                if(Var_String_Ipt[j+2]=="I"):
                    Many_FBI+=1
                    Arr_FBI.append(i+1)
                else:
                    pass
            else:
                pass
        else:
            pass
if(Many_FBI==0):
    print("HE GOT AWAY!")
else:
    for i in range(len(Arr_FBI)):
        print(Arr_FBI[i],end = ' ')
        

