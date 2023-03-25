parzyste1 = 0
parzyste2 = 0
nieparzyste1 = 0
nieparzyste2 = 0
pary = 0
ostatnie1 = []
ostatnie2 = []
podobne = 0
git1=0
git2=0
i=0

# ---------------Zadanie 4.1---------------
# with open("zadanie 2018/czerwiec/przyklad1.txt",'r') as f:
#     for line in f:
#         linijka1 = list(line.split())
#         ostatnie1.append(linijka1[len(linijka1)-1])
#         for i in linijka1:
#             if int(i)%2==0:
#                 parzyste1+=1
#             else: nieparzyste1+=1
#         if parzyste1==nieparzyste1==5:
#             git1+=1
#             parzyste1=nieparzyste1=0

# with open("zadanie 2018/czerwiec/przyklad2.txt",'r') as f:
#     for line in f:
#         linijka2 = list(line.split())
#         ostatnie2.append(linijka2[len(linijka2)-1])
#         for i in linijka2:
#             if int(i)%2==0:
#                 parzyste2+=1
#             else: nieparzyste2+=1

#         if parzyste2==nieparzyste2==5:
#             git2+=1
#             parzyste2=nieparzyste2=0

# for i in range(len(ostatnie1)):
#     if(ostatnie1[i]==ostatnie2[i]):
#         podobne+=1
# print("---------------Zadanie 4.1---------------")
# print(podobne)

# # ---------------Zadanie 4.2---------------
# print("---------------Zadanie 4.2---------------")
# pary = (git2+git1)/2
# print(pary)

# ---------------Zadanie 4.3---------------
print("---------------Zadanie 4.3---------------")
count=0
def licz_te_same(plik1,plik2):
    with open(plik1, 'r') as f1, open(plik2, 'r') as f2:
        
                        
    # return count
# print(licz_te_same("zadanie 2018/czerwiec/przyklad1.txt","zadanie 2018/czerwiec/przyklad2.txt"))




