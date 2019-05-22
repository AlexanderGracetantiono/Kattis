# this program is for open.kattis.com favourable
# this code currently still not accepted.
# this code is work on first text, then runtime error on the next test
# Doc:
# mains function is for searching which pages(list_page) that begin with page number (number)
# saves is for saving how many favourable ending ON a page that begin with x page number(number) this save on list_value with [page number,sumfav on this route]
# cari is for searching if there is a value(favourending) that have been done before, checking in list_value with key page number, and return sumfav on this route page
# searchs is actually the main function but, im to lazy to change so i made this documentation,, my code is fragile... back to topic,
# searchs function is for recursive searching the fav value on a page,, if its page number is end good fav++, other none. if the page we have is doesn't have value, then search in saves.. not found? do recursive..
# then save the value in saves.... so it can be used later...if you think that this make the code run slow.. well maybe,, delete it neither make it fast too IDK
# first thing first
# input
# first line is maximum cases you want 1? 2?
# next is number of the line you want to input either page or ending 4? 10?
# next line input is either 1 44 12 10, OR 3 favourable ,OR 6 Cataschropy...
# if the input is value it means page,, where 1 mean start page, and you can choose which next page you want to read 44 ? 12? or 10?
# example if you put another page value like 12 33 5 6 means if you choose 12, then it choose page start with 12, and have choice of page of 33 5 or 6
# output will be, how many good ending(favourable) in this BOOK, not one page,...
# Done

def mains(number):
    for n2 in range(len(list_page)):
        if(list_page[n2][0]==number):
            return n2

def saves(n_val):
    list_value.append(n_val)

def cari (num):
    for i in range(len(list_value)):
        if(list_value[i][0]==num):
            return int(list_value[i][1])
    return -1

def searchs(nin):
        fav=0
        for n3 in range(1,len(list_page[nin])):
            # print(list_page[nin][n3])
            cek='false'
            if(list_page[nin][n3]<=1):
                cek='true'
            if(cek=='false'):
                for nf in range(len(list_fav)):
                    if(list_page[nin][n3]==list_fav[nf]):
                        fav+=1
                        cek='true'
                        break
            if(cek=='false'):
                for nh in range(len(list_ends)):
                    if(list_page[nin][n3]==list_ends[nh]):
                        cek='true'
                        break
            if(cek=='false'):
                numsearch=list_page[nin][n3]
                carisave_val=cari(numsearch)
                if(carisave_val>-1):
                    fav+=carisave_val
                else:
                    sec=mains(numsearch)
                    tempfav=searchs(sec)
                    data=[list_page[nin][n3],tempfav]
                    saves(data)
                    fav+=tempfav
                cek='true'
        
        return fav
text='favourably'
# text='f'
cases=int(input())
for i in range(cases):
    section=int(input())
    list_fav=[0]*(0)
    list_page=[0]*(0)
    list_ends=[0]*(0)
    list_value=[0]*(0)
    for n in range(section):
        ipt=str(input()).split()
        if(len(ipt)>2):
            list_page.append([int(ipt[0]),int(ipt[1]),int(ipt[2]),int(ipt[3])])
        else:
            if(ipt[1]==text):
                list_fav.append(int(ipt[0]))
            else:
                list_ends.append(int(ipt[0]))
    fav=0
    fav+=searchs(0)
    # for n2 in range(len(list_page)):
    #     for n3 in range (len(list_fav)):
    #         if(list_page[n2]==list_fav[n3]):
    #             fav+=1
    #             break
    print(fav)