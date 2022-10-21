from traceback import print_tb

licz=[]
tablica = []
komenda = []
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
    if (podzial[len(podzial)-2] == podzial[len(podzial)-1]):
        new_func2()

    else:
        del podzial[:len(podzial)-1]

def new_func():
    global max_a
    global polecenie
    global i
    if (len(komenda)>i):
        # i = len(komenda)
        polecenie = komenda[(len(komenda)-1)]
        i += 1

    else:
        max_a = i

def new_func2():
    global max_b
    global literka
    global j
    if (len(podzial)>j):
        # i = len(komenda)
        literka = podzial[(len(podzial)-1)]
        j += 1

    else:
        max_b = j

def wystep():
    licz.append(podzial[1])

NAPIS = ""
j = 0
i = 0
x = 0
for line in linijki:
    x += 1
    podzial = line.split()
    if x >= len(linijki):
        break
    if podzial[0] == "DOPISZ":
        DOPISZ(podzial[1])
        komenda.append("dopisz")
        warunek()
        wystep()
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



print(tablica)
print(NAPIS.join(tablica)) #4.4
# print(len(tablica)) #4.1
print(komenda)
print(linijki[len(linijki) - 2]) 
print("Done!")
print(max_a, polecenie)        #4.2

