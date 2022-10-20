tablica = []
komenda = []
max_a =1
plik =  open('instrukcje.txt', 'r').read()
linijki = plik.split('\n')

def USUN_1():
    tablica.pop(len(tablica) - 1)

def DOPISZ(dp_lit):
    tablica.append(dp_lit)

def ZMIEN(zm_lit):
    tablica.pop(len(tablica) - 1)
    tablica.append(zm_lit)

def PRZESUN(pr_lit):
    x = tablica.index(pr_lit)
    if ord(tablica[x]) == 90:
        z = chr(65)
        tablica.pop(x)
        tablica.insert(x, z)
    else:
        z = chr(ord(tablica[x]) + 1)
        tablica.pop(x)
        tablica.insert(x, z)

def warunek():          #4.2
    if (komenda[len(komenda)-2] == komenda[len(komenda)-1]):
        
        new_func()

    else:
        del komenda[:len(komenda)-1]

def new_func():
    max_a = 2
    if (len(komenda)>max_a):
        max_a= len(komenda)
        print(max_a)
    else:
        max_a =2

        
try:
    for line in linijki:
        podzial = line.split()
        

        if podzial[0] == "DOPISZ":
            DOPISZ(podzial[1])
            komenda.append("dopisz")
            warunek()
        elif podzial[0] == "ZMIEN":
            ZMIEN(podzial[1])
            komenda.append("zmien")
            warunek()
        elif podzial[0] == "PRZESUN":
            PRZESUN(podzial[1])
            komenda.append("przesun")
            warunek()
        else:   
            USUN_1()
            komenda.append("usun")
            warunek()
    
except:
    # print(tablica) #4.4
    # print(len(tablica)) #4.1
    print("Done!")
    
