plik = open("liczby.txt",'r').read()
linijki = plik.split()
i=0
for line in linijki:
    i+=1
    print(i)
