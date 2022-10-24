from collections import Counter
tablica = []
komenda = []
wyst = []
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
        max_liczba_polecen()
    else:
        del komenda[:len(komenda)-1]

def max_liczba_polecen():
    global max_a
    global polecenie
    global i
    if (len(komenda)>i):
        polecenie = komenda[(len(komenda)-1)]
        i += 1
    else:
        max_a = i

NAPIS = ""
k = 0
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
        wyst.append(podzial[1])
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

    counter = Counter(wyst)

# print(tablica)
print(len(tablica))             #4.1
print(max_a, polecenie)         #4.2
print(counter)                  #4.3
print(NAPIS.join(tablica))      #4.4
print("Done!")