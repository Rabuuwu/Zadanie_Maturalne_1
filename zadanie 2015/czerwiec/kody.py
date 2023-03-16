values = []
with open('zadanie 2015/czerwiec/cyfra_kodkreskowy.txt', 'r') as file:
    for line in file:
        values.append(line.strip())

with open('zadanie 2015/czerwiec/kody.txt', 'r') as a:
    liczba = a.readline().strip()
# ------------Zadanie 6.1 ------------------
# Inicjalizujemy zmienne dla sumy cyfr w pozycji parzystej i nieparzystej
even_sum = 0
odd_sum = 0

for i, digit in enumerate(liczba):
    if i % 2 == 0:  
        odd_sum += int(digit)
    else: 
        even_sum += int(digit)

# Obliczamy wynik końcowy
result = 3 * even_sum + odd_sum
reszta=result%10
roznica =10-reszta
control = roznica%10
kontrolna = values[control]

# Wyświetlamy wynik na ekranie
print("------------Zadanie 6.1 ------------------")
print(f'Suma cyfr w pozycji parzystej, pomnożona przez 3, to: {3 * even_sum}')
print(f'Suma cyfr w pozycji nieparzystej, to: {odd_sum}')
print(f'Wynik końcowy to: {result}')


  # odczytanie liczby z pliku i usunięcie ewentualnych białych znaków

cyfry = [int(c) for c in liczba]  # zamiana każdej cyfry z łańcucha znaków na liczbę i umieszczenie jej w liście
l=""
start="11011010 "
stop=" 11010110"
print(cyfry)  # wyświetlenie listy cyfr
for i in cyfry:
    l+=str(values[i])+" "
print(start+l+kontrolna+stop)




# start 11011010
# stop 11010110 
# 0 10101110111010 
# 1 11101010101110 
# 2 10111010101110 
# 3 11101110101010 
# 4 10101110101110 
# 5 11101011101010 
# 6 10111011101010 
# 7 10101011101110 
# 8 11101010111010 
# 9 10111010111010