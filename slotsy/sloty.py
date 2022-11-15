import random
#           odczytywanie kaksi
odczyt = open("kasa.txt",'r')
kasa = odczyt.readline()
kasa = int(kasa)
odczyt.close()

#           wpisanie ilości liczb w slotach
amount = input("na ilu slotach chcesz zagrac? (3? a moze 5?)")
amount= int(amount)
flag=0
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
    
#           slotsy
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
#           JACKPOT
if flag==1:
    print("JACKPOT!")
    kasa = kasa + 10000
if flag==2:
    print("JACKPOT!")
    kasa = kasa + 50000

#           test odczytu  i nadpisanie kaski
print(kasa)
#           otwierania pliku do nadpisania kaski po grze
zapis = open("kasa.txt",'w+')
zapis.write(str(kasa))