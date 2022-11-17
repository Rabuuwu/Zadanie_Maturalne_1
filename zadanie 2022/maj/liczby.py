plik =  open('liczby.txt', 'r').read()
linijki = plik.split('\n')
tablica=[]
x = -1
d=0
a=0
def rozloz(n):
    czynniki = []
    global d
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k += 1

    if(len(czynniki)> d):
        d = len(czynniki)
        # print(n, d)
        print(y, len(czynniki))
    
    return czynniki
    
for line in linijki:
    x += 1
    if x >= len(linijki):
        break
    y=linijki[x]
    n = int(y)
    # print(n)
    rozloz(n)
    if y[0] == y[len(y)-1]:
        tablica.append(y)
    liczba1 = linijki[x]
    liczba2 = linijki[(x+1)]
    liczba3 = linijki[(x+2)]   
# print(tablica)      #4.1
    if(int(liczba2)%int(liczba1) ==0):
        if(int(liczba3)&int(liczba2) ==0):  
            print(liczba1, liczba2, liczba3)
    a+=1