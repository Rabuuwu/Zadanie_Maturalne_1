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

with open('zadanie 2019\czerwiec\liczby.txt', 'r') as f:
    for line in f:
        number = int(line.strip())
        if is_prime(number):
            if(number>=100 and number<=5000):
                prime_numbers.append(number)
print("------------Zadanie 4.1 ------------------")
print("Liczby pierwsze: ", prime_numbers)

# ------------Zadanie 4.2 ------------------

pierwsze=[]
with open('zadanie 2019\czerwiec\pierwsze.txt', 'r') as f:
    for line in f:
        number = int(line.strip())
        reversed_number = int(str(number)[::-1])  # odwrócenie cyfr liczby
        if is_prime(number) and is_prime(reversed_number):
            pierwsze.append(number)
print("------------Zadanie 4.2 ------------------")
print("Liczby pierwsze rowniez po odwroceniu: ",pierwsze)
print("------------Zadanie 4.3 ------------------")
# ------------Zadanie 4.3 ------------------
pojed=0
with open('zadanie 2019\czerwiec\pierwsze.txt', 'r') as f:
    for line in f:
        lis=list(line.strip())
        res =[eval(n) for n in lis]
        suma1=sum(res)
        print(suma1)
        if suma1==1:
            pojed +=1
        if suma1>9:
            lis1=list(str(suma1).strip())
            res2=[eval(n) for n in lis1]
            suma=sum(res2)
            print(suma)
            if suma==1:
                pojed +=1
            if suma>9:
                lis2=list(str(suma).strip())
                res3=[eval(n) for n in lis2]
                suma2=sum(res3)
                print(suma2)
                if suma2==1:
                    pojed +=1
print("ilosc liczb z waga 1: ",pojed)

# ------------Zadanie 4.4 ------------------

