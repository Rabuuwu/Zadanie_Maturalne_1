#           Zadanie 6.1

# plik = open("przyklad.txt",'r').read().split()
# piksele = [eval(i) for i in plik]
# print(min(piksele))
# print(max(piksele)) #6.1

#           Zadanie 6.2

# plik = open("przyklad.txt",'r').read()
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

plik = open("przyklad.txt",'r').read()
linijki = plik.split('\n')
i=0
j=0
liczba = 0
kontarstujace=0
pixele = [[ [''] for a in range(320)] for b in range(200)]

# print(pixele)

def isPixelContrasting(pixel1, pixel2):
    if((int(pixel1)-int(pixel2))>128):
        return true
    else:
        return false

for line in linijki:
    podzial = line.split()
    if line == '':
        break
    else:
        for j in range(320):
            if j==320:
                break
            else:
                pixele[i][j] = podzial[j]
       
                for a in range(200):
                    a+=1
                    if a>0 and isPixelContrasting(str(pixele[a-1][j]),str(pixele[a][j])):
                        kontrastujace+=1
                    elif a<199 and isPixelContrasting(str(pixele[a+1][j]),str(pixele[a][j])):
                        kontarstujace+=1
                    elif j>0 and isPixelContrasting(pixele[a-1][j],pixele[a][j]):
                        kontarstujace+=1
                    elif j<319 and isPixelContrasting(pixele[a][j+1],pixele[a][j]):
                        kontarstujace+=1
    i+=1 
print(kontarstujace)


# int countContrastingPixels(int data[][320]) {
#     int contrastingPixels = 0;
#     for(int i = 0;i<200;i++) {
#         for(int j = 0;j<320;j++) {
#             if(i>0 && isPixelContrasting(data[i-1][j],data[i][j])) {
#                 contrastingPixels++;
#             }
#             else if(i<199 && isPixelContrasting(data[i+1][j],data[i][j])) {
#                 contrastingPixels++;
#             }
#             else if(j>0 && isPixelContrasting(data[i][j-1],data[i][j])) {
#                 contrastingPixels++;
#             }
#             else if(j<319 && isPixelContrasting(data[i][j+1],data[i][j])) {
#                 contrastingPixels++;
#             }
#         }
#     }
#     return contrastingPixels;
# }