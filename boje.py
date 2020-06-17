slovo = str(input())
l = []

r1 = str(input())
l.append(list(r1))
r2 = str(input())
l.append(list(r2))
r3 = str(input())
l.append(list(r3))
r4 = str(input())
l.append(list(r4))
r5 = str(input())
l.append(list(r5))

for red in range(5):    #zamjenjivanje određene boje X-om
    for stupac in range(5):
        if l[red][stupac] == slovo:
            l[red][stupac] = "X"


for stupac in range(5):     #utjecaj gravitacije na boje
    for red in range(5):
        if l[red][stupac] == "X":
            k = red
            while k > 0:
                l[k][stupac] = l[k-1][stupac]
                k -= 1
                
            l[0][stupac] = "X"

for i in range(5):  #ispisivanje tablice u redovima
    razmak = ""
    a = razmak.join(l[i])
    print (a)





        
