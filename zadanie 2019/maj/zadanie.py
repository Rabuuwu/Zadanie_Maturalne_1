import math
plik = open("zadanie 2019\maj\liczby.txt",'r').read()
linijki = plik.split()
nwd=[1]
liczby=[]
potegi=[]

# ------------Zadanie 4.1 ------------------
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    if number == 1:
      return True

    else:return False
  # Recursive case: keep dividing number by base.
  return is_power_of(number/base , base)

# ------------Zadanie 4.2 ------------------
def silnia(n): return n*silnia(n-1) if n > 1 else 1
def rozdziel(n):
    global lista
    global lista2
    global a
    lista2 =[]
    global o
    lista = list(str(n))
    for o in lista:
        lista2.append(silnia(int(o)))
        a=sum(lista2)
        if a==n:
            print(n)
print("------------Zadanie 4.2 ------------------")

for i in linijki:
    n=int(i)
    if(is_power_of(n,3) == True):
        potegi.append(n)
    rozdziel(n)

print("------------Zadanie 4.1 ------------------")
print(potegi)

print("------------Zadanie 4.3 ------------------")
# ------------Zadanie 4.3 ------------------
for x in range(len(linijki)):
  if x!=0:
     if x!=(len(linijki)-1):
        liczba_1 = int(linijki[x-1])
        liczba_2 = int(linijki[x])
        liczba_3 = int(linijki[x+1])
        z=math.gcd(liczba_1,liczba_2,liczba_3)
        if (z!=nwd[0] or z>=nwd[0]) and (z>1 and z>=nwd[0]):  
          nwd.clear()
          if len(liczby)>2:
             liczby.remove(liczby[0])
          nwd.append(z), liczby.extend([liczba_1,liczba_2,liczba_3])
     if x==(len(linijki)-1):
        liczba_1 = int(linijki[x-2])
        liczba_2 = int(linijki[x-1])
        liczba_3 = int(linijki[x])
        z=math.gcd(liczba_1,liczba_2,liczba_3)
        if (z!=nwd[0] and z>nwd[0]) and (z>1 and z>=nwd[0]):  
          nwd.clear()
          liczby.remove(liczby[0])
          liczby.remove(liczby[0])
          nwd.append(z), liczby.extend([liczba_1,liczba_2,liczba_3])

output = []
for g in liczby:
    if g not in output:
        output.append(g)
ciag=[]
for h in range (len(output)):
   if int(output[h])%int(nwd[0])==0:
      ciag.append(output[h])

print(ciag[0])
print(len(ciag))
print(nwd)