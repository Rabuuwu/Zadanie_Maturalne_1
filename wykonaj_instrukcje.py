tablica = []

plik =  open('instrukcje.txt', 'r').read()
linijki = plik.split('\n')
for line in linijki:
        print(tablica)
        podzial = line.split()

        def USUN_1():
            tablica.pop(len(tablica) - 1)
    
        def DOPISZ(dp_lit):
            tablica.append(dp_lit)

        def ZMIEN(zm_lit):
            tablica.pop(len(tablica) - 1)
            tablica.append(zm_lit)
    
        def PRZESUN(pr_lit):
            x = tablica.index(pr_lit)
            z = chr(ord(tablica[x]) + 1)
            tablica.pop(x)
            tablica.insert(x, z)


        if podzial[0] == "DOPISZ":
            DOPISZ(podzial[1])
            
        elif podzial[0] == "ZMIEN":
            ZMIEN(podzial[1])
            
        elif podzial[0] == "PRZESUN":
            PRZESUN(podzial[1])
            
        else:   
            USUN_1() 
        


# zmienna = "płotek"
# print(zmienna[len(zmienna) - 1])

# DOPISZ("A")
# DOPISZ("B")
# DOPISZ("C")
# DOPISZ("D")


# b = tablica.index("A")
# print(b)
# tablica.pop(b)
# c = tablica.index("B")
# print(c)
        
