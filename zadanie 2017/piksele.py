#           Zadanie 6.1

plik = open("dane.txt",'r').read().split()
piksele = [eval(i) for i in plik]
print(min(piksele))
print(max(piksele))

#           Zadanie 6.2

# plik = open("dane.txt",'r').read()
# linijki = plik.split('\n')
# flag = 0
# y = 0 
# for line in linijki:
#     podzial = line.split()
#     y += 1
#     x = 0
#     while x in range((len(podzial))//2):
#         if podzial[x] != podzial[len(podzial)-1-x]:
#             flag += 1
#             break
#         x += 1
# print(flag)

#           Zadanie 6.3

# import math
 
# def nearContrasting(x, y, all):
#     if x != 0:
#         if math.fabs(all[x][y] - all[x-1][y]) > 128:
#             return True
#     if x != 199:
#         if math.fabs(all[x][y] - all[x + 1][y]) > 128:
#             return True
#     if y != 319:
#         if math.fabs(all[x][y] - all[x][y+1]) > 128:
#             return True
#     if y != 0:
#         if math.fabs(all[x][y] - all[x][y-1]) > 128:
#             return True
#     return False
 
# file = open("dane.txt", "r").read().split('\n')
# all = [[0 for x in range(320)] for y in range(200)]
# counter = 0
# contrasting = 0
# for line in file:
#     if len(line.split(" ")) < 2 or len(line.split(" ")[1]) < 1:
#         continue
#     points = line.split(" ")
#     for i in range(320):
#         all[counter][i] = int(points[i])
#     counter +=1
# for i in range(200):
#     for j in range(320):
#         if nearContrasting(i, j, all):
#             contrasting += 1
# print("Punktow kontrastujacych: " + str(contrasting))

#           Zadanie 6.4

# file = open("dane.txt", "r").read().split('\n')
# all = [[0 for x in range(200)] for y in range(320)]
# counter = 0
# inline = 0
# for line in file:
#     if len(line.split(" ")) < 2 or len(line.split(" ")[1]) < 1:
#         continue
#     points = line.split(" ")
#     for i in range(320):
#         all[i][counter] = int(points[i])
#     counter +=1
# for i in range(320):
#     cmax = 0
#     c = 0
#     for j in range(200):
#         if all[i][j] == all[i][j-1]:
#             c += 1
#         else:
#             if c > cmax:
#                 cmax = c+1
#             c = 0
#     if inline < cmax:
#         inline = cmax

# print("Najdluzsza kolumna pixeli tego samego koloru: " + str(inline))