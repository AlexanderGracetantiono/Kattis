statement_s_e_n = input().split(" ")
statement_di = input().split(" ")
statement_bi=input().split(" ")
statement_ci =input().split(" ")
sumTime =int(statement_s_e_n[0])
for i in range(int(statement_s_e_n[2])):
    sumTime +=int(statement_di[i]) 
    # print(sumTime,end="/time \n")
    if((sumTime%int(statement_ci[i]))!=0):
        residue = int(statement_ci[i])-(sumTime%int(statement_ci[i]))
    # print(sumTime%int(statement_ci[i]),end="/res1 \n")
    # print(int(statement_ci[i]),end="/res2 \n")
    # print(residue,end="/res \n")
    sumTime +=residue + int(statement_bi[i])
    # print(sumTime,end="/time \n")
sumTime+=int(statement_di[int(statement_s_e_n[2])])
# print(sumTime,end="/timeEnd \n")
if(sumTime>int(statement_s_e_n[1])):
    print("no")
else:
    print("yes")

    
        




#     Var_String_Ipt = input()
#     for j in range(len(Var_String_Ipt)):
#         # print("data: ",Var_String_Ipt[j])
#         if(Var_String_Ipt[j] == "F"):
#             if(Var_String_Ipt[j+1]=="B"):
#                 if(Var_String_Ipt[j+2]=="I"):
#                     Many_FBI+=1
#                     Arr_FBI.append(i+1)
#                 else:
#                     pass
#             else:
#                 pass
#         else:
#             pass
# if(Many_FBI==0):
#     print("HE GOT AWAY!")
# else:
#     for i in range(len(Arr_FBI)):
#         print(Arr_FBI[i],end = ' ')
        

