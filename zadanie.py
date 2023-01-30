plik = open("liczby.txt",'r').read()
linijki = plik.split()
i=0
a=0
b=0
zero=0
jeden=0

podzielne2=0
podzielne8=0
lzer=[]
ljed=[]

def zad1(line):
    zero=0
    jeden=0
    global a
    for letter in line:
        if letter=='1':
            jeden+=1
        else:zero+=1
    if zero>jeden:
        a+=1
    zero=0
    jeden=0
    

def zad2(line):
    linia = int(line)
    global podzielne2
    global podzielne8
    if linia %2 ==0:
        podzielne2+=1
    if linia%8==0:
        podzielne8+=1


def zad3(linijki):
    global minimum
    global maximum

    maximum = linijki.index(max(linijki))
    minimum = linijki.index(min(linijki))


for line in linijki:
    zad1(line)
    zad2(line)
    zad3(linijki)




print("----------Zadanie 1 -----------")
print(a)
print("----------Zadanie 2 -----------")
print("Podzielne przez 2: ",podzielne2)
print("Podzielne przez 8: ",podzielne8)
print("----------Zadanie 3 -----------")
print()

