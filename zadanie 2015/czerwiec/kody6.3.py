values = []
with open('zadanie 2015/czerwiec/cyfra_kodkreskowy.txt', 'r') as file:
    for line in file:
        values.append(line.strip())

with open('zadanie 2015/czerwiec/kody.txt', 'r') as input_file:
    with open('zadanie 2015/czerwiec/kody1.txt', 'w') as output_file:
        for line in input_file:
            liczba = line.strip()

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
            reszta = result % 10
            roznica = 10 - reszta
            control = roznica % 10
            kontrolna = values[control]

            cyfry = [int(c) for c in liczba]  # zamiana każdej cyfry z łańcucha znaków na liczbę i umieszczenie jej w liście
            l = ""
            start = "11011010 "
            stop = " 11010110"
            for i in cyfry:
                l += str(values[i]) + " "
            output_file.write(start + l + kontrolna + stop + '\n')





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