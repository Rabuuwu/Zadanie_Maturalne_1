liczby=0
i=0
napis=""
a=0
b=1
l = ['0','1','2','3','4','5','6','7','8','9']
with open("zadanie 2021/czerwiec/przyklad.txt",'r') as file:
    for line in file:
        linijka = [char for char in line]
        if b%20==0:
            if a < 50:
                napis=napis+linijka[a]
                a+=1
        for i in range(len(linijka)):
            if linijka[i] in l:
                liczby+=1
        b+=1

print(liczby)
print (napis)