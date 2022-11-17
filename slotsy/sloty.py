import random

#           sprawdzanie wygranej dla 3 liczb
def trzy():
    global flag
    if sloty[0] == sloty[1] == sloty[2]:
        print(sloty)
        flag=1
    else:print(sloty)

#           sprawdzanie wygranej dla 5 liczb
def piec():
    global flag
    if sloty[0] == sloty[1] == sloty[2] == sloty[3] == sloty[4]:
        print(sloty)
        flag=2
    else:print(sloty)

#           JACKPOT    
def jackpot():
    if flag != 0:
        print("JACKPOT!")
    if flag==1:
        kasa = kasa + 10000
        print("Wygrales: 10000")
    if flag==2:
        kasa = kasa + 50000
        print("Wygrales: 50000")    
#           slotsy
def gra():
    global sloty
    global flag
    #           odczytywanie kaksi
    odczyt = open("./slotsy/kasa.txt",'r')
    kasa = odczyt.readline()
    kasa = int(kasa)
    odczyt.close()

    #           wpisanie ilości liczb w slotach
    amount = input("na ilu slotach chcesz zagrac? (3? a moze 5?)")
    amount= int(amount)
    flag=0

    if kasa <300:
        print("Nie maz kasy!")
    else:
        if amount == 3:
            kasa = kasa - 300
        if amount == 5:
            kasa = kasa - 500
        for i in range(3):
            sloty = [random.randint(1,7) for x in range(amount)]
            if amount == 3:
               trzy()
            if amount == 5:
               piec()
    jackpot()     
    #           test odczytu  i nadpisanie kaski
    print(kasa)

    #           otwierania pliku do nadpisania kaski po grze
    zapis = open("./slotsy/kasa.txt",'w+')
    zapis.write(str(kasa))


gra()


