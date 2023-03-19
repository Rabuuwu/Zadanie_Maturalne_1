# ------------Zadanie 4.1 ------------------
liczby=[]
with open('zadanie 2023\liczby.txt', 'r') as file:
    for line in file:
        number = line.strip() # Usunięcie białych znaków na początku i końcu linii
        if number[:2] == number[-2:]: # Sprawdzenie, czy początkowe i końcowe dwie cyfry są takie same
            liczby.append(number) # Wypisanie liczby, jeśli spełnia warunek
print("------------Zadanie 4.1 ------------------")
print(len(liczby)+1)

# ------------Zadanie 4.2 ------------------
def is_prime(n):
    # """Funkcja sprawdzająca, czy liczba jest pierwsza."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = []

with open('zadanie 2023\liczby.txt', 'r') as f:
    for line in f:
        hex_number = line.strip()
        dec_number = int(hex_number,16)
        if is_prime(dec_number):
            prime_numbers.append(hex_number)
print("------------Zadanie 4.2 ------------------")
print(len(prime_numbers)+1)

# ------------Zadanie 4.4 ------------------
prev_number = 0
order=[]
maxi=[]
with open('zadanie 2023\liczby.txt', 'r') as f:
    for line in f:
        hex_number = line.strip()
        dec_number = int(hex_number,16)
        if dec_number > prev_number:
            order.append(dec_number)
            prev_number = dec_number
            maxi.append(len(order))
        if dec_number <prev_number:
            maxi.clear()
            order.clear()
            order.append(dec_number)
            prev_number = dec_number
            maxi.append(len(maxi))
print("------------Zadanie 4.4 ------------------")
print(order)
print(max(maxi))

