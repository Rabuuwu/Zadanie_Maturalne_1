# ------------Zadanie 4.1 ------------------
def is_prime(n):
    # """Funkcja sprawdzająca, czy liczba jest pierwsza."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = []

with open('zadanie 2019\czerwiec\liczby_przyklad.txt', 'r') as f:
    for line in f:
        number = int(line.strip())
        if is_prime(number):
            if(number>=100 and number<=5000):
                prime_numbers.append(number)
print("------------Zadanie 4.1 ------------------")
print("Liczby pierwsze: ", prime_numbers)

# ------------Zadanie 4.2 ------------------

pierwsze=[]
with open('zadanie 2019\czerwiec\pierwsze_przyklad.txt', 'r') as f:
    for line in f:
        number = int(line.strip())
        reversed_number = int(str(number)[::-1])  # odwrócenie cyfr liczby
        if is_prime(number) and is_prime(reversed_number):
            pierwsze.append(number)
print("------------Zadanie 4.2 ------------------")
print("Liczby pierwsze rowniez po odwroceniu: ",pierwsze)

# ------------Zadanie 4.3 ------------------
with open('zadanie 2019\czerwiec\pierwsze_przyklad.txt', 'r') as f:
    for line in f:
        lis=list(line.strip())
        res =[eval(n) for n in lis]
        suma1=sum(res)
        print(suma1)
        if suma1>9:
            lis1=list(str(suma1).strip())
            res=[eval(n) for n in lis1]
            suma=sum(res)
            print(suma)
# print("------------Zadanie 4.3 ------------------")
# print(suma)
