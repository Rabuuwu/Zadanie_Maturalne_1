plik = open("sygnaly.txt",'r').read()
linijki = plik.split()
x=-1
y=-1
index = 39
for line in linijki:
    x+=1
    if index == x:    
        # print(line[9])
        index+=40
    y+=1
    z=0
    string = linijki[y]
    unikalne =[]
    for literka in line:
        if line[z] not in unikalne:
            unikalne.append(line[z])
        z+=1
        dlugosc = 0
        if len(unikalne)>dlugosc:
            dlugosc  = len(unikalne)
print(y, unikalne, dlugosc)