tablica = []
komenda = []
i=1
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
        print(komenda)
        if (i>max_a):
            max_a=i
            print(max_a)
        else:
            i+=1
    else:
        del komenda[:len(komenda)-1]
        print(komenda)
        
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
    # print(tablica)
    # print(len(tablica)) #4.1
    #  
    print("Done!")