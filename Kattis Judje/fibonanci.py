i=0
n1=0
n2=1
while i<12:
    print(n1,end=' , ')
    nth=n1+n2
    n1=n2
    n2=nth
    i=i+1
xx=-1
while xx!=0:
    print("Menu\n1.Persegi Panjang\n2.Segitiga\n0.Keluar")
    xx=int(input())
    if xx==0:
        print("Terima Kasih")

    elif xx==1:
        print("Masukan Panjang: ")
        p=int(input())
        print("Masukan lebar")
        l=int(input())
        print("luas Persegi Panjang",p*l)
    else:
        print("Masukan Alas: ")
        a=int(input())
        print("Masukan Tinggi")
        t=int(input())
        print("luas Segitiga",(a*t)/2)