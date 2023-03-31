import math

litery = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
kod = []
k=107

# with open("zadanie 2016/maj/dane_6_1.txt", "r") as f:
#     for line in f:
#         linia = line.split()
#         wiersz = str(linia[0])
#         literki = list(wiersz)
#         i=0
#         for i in range(len(literki)):
#             x= litery.index(literki[i])
#             y=x+k
#             z=y%26
#             kod.append(litery[z])
#         print(kod)
#         kod.clear()

with open("zadanie 2016/maj/dane_6_2.txt", "r") as f:
    for line in f:
        linia = line.split()
        wiersz = str(linia[0])
        l=int(linia[1])
        literki = list(wiersz)
        i=0
        