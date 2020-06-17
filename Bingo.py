
n = int(input())
ivan = []
stjepan = []
gustav = []
a,b,c = map(int,input().split())
for i in range(n):      #unos brojeva koje imaju igraci
    ivan.append(a+i)
    stjepan.append(b+i)
    gustav.append(c+i)


m = int(input())
brojevi = []
for i in range(m):      #dobiveni brojevi
    broj = int(input())
    brojevi.append(broj)


ivan_bodovi = 0
stjepan_bodovi = 0
gustav_bodovi = 0

bodovano = []

for i in range(len(brojevi)):
    
    if brojevi[i] in ivan and brojevi[i] not in bodovano:
        ivan_bodovi += 1
    if brojevi[i] in stjepan and brojevi[i] not in bodovano:
        stjepan_bodovi += 1
    if brojevi[i] in gustav and brojevi[i] not in bodovano:
        gustav_bodovi += 1
    bodovano.append(brojevi[i])


if ivan_bodovi > gustav_bodovi and ivan_bodovi > stjepan_bodovi:
    print ("Ivan")
elif stjepan_bodovi > gustav_bodovi and stjepan_bodovi > ivan_bodovi:
    print ("Stjepan")
elif gustav_bodovi > ivan_bodovi and gustav_bodovi > stjepan_bodovi:
    print ("Gustav")
else:
    print ("Goran")