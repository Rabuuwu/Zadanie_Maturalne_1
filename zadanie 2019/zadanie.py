# import math
# plik = open("zadanie 2019\przyklad.txt",'r').read()
# linijki = plik.split()

# potegi=[]

# # ------------Zadanie 4.1 ------------------
# def is_power_of(number, base):
#   # Base case: when number is smaller than base.
#   if number < base:
#     # If number is equal to 1, it's a power (base**0).
#     if number == 1:
#       return True

#     else:return False
#   # Recursive case: keep dividing number by base.
#   return is_power_of(number/base , base)

# # ------------Zadanie 4.2 ------------------
# def silnia(n): return n*silnia(n-1) if n > 1 else 1
# def rozdziel(n):
#     global lista
#     global lista2
#     global a
#     lista2 =[]
#     global o
#     lista = list(str(n))
#     for o in lista:
#         lista2.append(silnia(int(o)))
#         a=sum(lista2)
#         if a==n:
#             print(n)
# print("------------Zadanie 4.2 ------------------")

# for i in linijki:
#     n=int(i)
#     if(is_power_of(n,3) == True):
#         potegi.append(n)
#     rozdziel(n)

# print("------------Zadanie 4.1 ------------------")
# print(potegi)
import math
with open('zadanie 2019\przyklad.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f]

longest_sequence = []
current_sequence = []

for i in range(len(numbers) - 1):
    if numbers[i+1] == numbers[i] + 1:
        current_sequence.append(numbers[i])
    else:
        current_sequence.append(numbers[i])
        gcd = current_sequence[0]
        for num in current_sequence:
            gcd = math.gcd(gcd, num)
        if gcd > 1 and len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence
        current_sequence = []

if current_sequence:
    current_sequence.append(numbers[-1])
    gcd = current_sequence[0]
    for num in current_sequence:
        gcd = math.gcd(gcd, num)
    if gcd > 1 and len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

first_number = longest_sequence[0]
sequence_length = len(longest_sequence)
gcd = longest_sequence[0]
for num in longest_sequence:
    gcd = math.gcd(gcd, num)

print(first_number, sequence_length, gcd)
