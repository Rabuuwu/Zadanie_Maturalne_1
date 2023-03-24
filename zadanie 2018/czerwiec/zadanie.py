ostatnie1 = []
ostatnie2 = []
podobne =0
with open("zadanie 2018/czerwiec/przyklad1.txt",'r') as f:
    for line in f:
        linijka1 = list(line.split())
        ostatnie1.append(linijka1[len(linijka1)-1])
        # print(linijka1)
        # print(ostatnie1)

with open("zadanie 2018/czerwiec/przyklad2.txt",'r') as f:
    for line in f:
        linijka2 = list(line.split())
        ostatnie2.append(linijka2[len(linijka2)-1])
        # print(linijka2)
        # print(ostatnie2)
i=0
for i in range(len(ostatnie1)):
    if(ostatnie1[i]==ostatnie2[i]):
        podobne+=1
print(podobne)