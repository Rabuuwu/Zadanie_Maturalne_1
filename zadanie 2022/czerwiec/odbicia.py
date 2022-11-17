import math

plik =  open('liczby.txt', 'r').read()
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
    

def main():
    global line
    for line in linijki:
        if line == "":
            break
        else:
            odbicie()
            odejmowanie()
            
main()
print("Max: " + str(max(roznica)))