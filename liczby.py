

plik =  open('liczby.txt', 'r').read()
linijki = plik.split('\n')
tablica=[]
x = -1


for line in linijki:
    x += 1
    if x >= len(linijki):
        break
    y=linijki[x]
    if y[0] == y[len(y)-1]:
        tablica.append(y)
        # print(tablica)      #4.1

