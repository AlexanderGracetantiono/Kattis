ipt1 = 1
while (True):
    k_res = ""
    ipt1 = str(input())
    if (ipt1 == "0"):
        break
    else:
        ipt1 =ipt1.split()
        rota = int(ipt1[0])
        ob = str(ipt1[1])
        # Reverse First
        k_reverse=""
        for a in ob:
            k_reverse = a + k_reverse
        # Next, add the numbe
        for i in k_reverse:
            t_ord = ord(i)
            if (t_ord == 95):
                t_chr_num = 91 + rota
            elif (t_ord == 46):
                t_chr_num = 92 + rota
            else:
                t_chr_num = t_ord + rota
            if (t_chr_num > 92):
                t_chr_num = (t_chr_num % 92) + 64
            if (t_chr_num == 91):
                t_chr_num = 95
            if (t_chr_num == 92):
                t_chr_num = 46
            k_res += chr(t_chr_num)
        print(k_res)

