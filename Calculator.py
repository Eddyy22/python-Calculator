def Toplama():
    print(sayi1,"+",sayi2,"=",sayi1+sayi2)

def Cikarma():
    print(sayi1,"-",sayi2,"=",sayi1-sayi2)

def Carpma():
    print(sayi1,"*",sayi2,"=",sayi1*sayi2)

def Bolme():
    print(sayi1,"/",sayi2,"=",sayi1/sayi2)

while True:
    print("""
***********
1. Toplama
2. Cikarma
3. Carpma
4. Bolme
5. Cikis
***********
""")
    sayi1 = int(input("1. Sayiyi girin :"))
    sayi2 = int(input("2. Sayiyi girin :"))
    islem = int(input("Islem Turunu Secin :"))
    if islem == 1:
        Toplama()
        break
    if islem == 2:
        Cikarma()
        break
    if islem == 3:
        Carpma()
        break
    if islem == 4:
        Bolme()
        break
    if islem == 5:
        quit()
    