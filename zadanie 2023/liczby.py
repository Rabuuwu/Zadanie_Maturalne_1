import random

with open('liczby.txt', 'w') as f:
    for i in range(3000):
        n = random.randint(1, 1000000000)
        hex_n = hex(n)[2:].upper()
        f.write(hex_n + '\n')
