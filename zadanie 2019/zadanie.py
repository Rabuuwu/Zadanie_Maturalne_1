import math
plik = open("zadanie 2019\liczby.txt",'r').read()
linijki = plik.split()
# ------------Zadanie 4.2 ------------------
def silnia(n): return n*silnia(n-1) if n > 1 else 1

def rozdziel(n):
    global lista
    global lista2
    global a
    lista2 =[]
    global o
    lista = list(str(n))
    for o in lista:
        lista2.append(silnia(int(o)))
        a=sum(lista2)
        if a==n:
            print(n)
print("------------Zadanie 4.2 ------------------")
for i in linijki:
    n=int(i)
    rozdziel(n)
    