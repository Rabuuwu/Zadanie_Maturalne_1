plik = open("dane.txt",'r').read().split()
piksele = [eval(i) for i in plik]
print(min(piksele))
print(max(piksele)) #6.1

# x = -1
# z=0
# a=255
# for line in linijki:
#     x+=1
#     podzial = line.split()
#     if int(a)>int(podzial[0]):
#         a = int(podzial[0])
#     elif int(z)<int(podzial[0]):
#         z=int(podzial[0])
# print(a, z)         #6.1
