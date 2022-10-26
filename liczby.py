

plik =  open('liczby.txt', 'r').read()
linijki = plik.split('\n')
tablica=[]
x = -1
d=0
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
        print(czynniki)
    
    return czynniki
    
for line in linijki:
    x += 1
    if x >= len(linijki):
        break
    y=linijki[x]
    n = int(y)
    print(n)
    rozloz(n)
    if y[0] == y[len(y)-1]:
        tablica.append(y)

# print(tablica)      #4.1
    