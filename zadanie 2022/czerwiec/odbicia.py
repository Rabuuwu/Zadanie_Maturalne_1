import math

plik =  open('zadanie 2022\czerwiec\liczby.txt', 'r').read()
linijki = plik.split('\n')
roznica = []

def odbicie(): #4.1
    global liczba1
    liczba1 = line[::-1]
    if int(liczba1) % 17 == 0:
        print (liczba1)

def odejmowanie(): #4.2
    global liczba2
    global liczba3
    liczba2 = line
    liczba2 = int(liczba2)
    liczba3 = line[::-1]
    liczba3 = int(liczba3)
    wynik = abs(liczba2-liczba3)
    roznica.append(wynik)

def czy_pierwsza(n, n2):
    for i in range(2, n):
        if n % i == 0:
            return False
        for i in range(2, n2):
            if n2 % i == 0:
                return False
    print(n)

def odpal_czy_pierwsza():
    for line in linijki:
            if line == "":
                break
            else:
                czy_pierwsza(int(line), int(line[::-1]))

def maximum(): #4.2
    index = roznica.index(max(roznica))
    print("Max: " + str(linijki[index]) +" "+  str(max(roznica)))

def liczenie(): #4.4 policzenie roznych, powtarzających sie 2 razy, powt 3  razy
    checked=[]
    count=[]
    for i in range(len(linijki)):
        if linijki[i] not in checked:
            count.append([ linijki[i], linijki.count(linijki[i]) ])
            checked.append(linijki[i])

    rozne=len(count)
    podwojne=len([i for i in count if i[1]==2])
    potrojne=len([i for i in count if i[1]==3])
    print(rozne, podwojne, potrojne)



def main():
    global line
    for line in linijki:
        if line == "":
            break
        else:
            odbicie()
            odejmowanie()
            
def skrypt():
    print("---------4.1---------")            
    main()
    print("---------4.2---------")
    maximum()
    print("---------4.3---------")
    odpal_czy_pierwsza()
    print("---------4.4---------")
    liczenie()
    print("---------------------")


skrypt()

