import math
plik = open("zadanie 2019\maj\przyklad.txt",'r').read()
linijki = plik.split()

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


