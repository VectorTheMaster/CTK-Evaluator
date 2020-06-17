l = [] #lista za brojeve
l1 = [] #lista za jokere

a,b,c,d,e,f = map(int, input().split())
zadnja_znamenka = repr(a)[-1]
zadnja_znamenka1 = repr(b)[-1]
zadnja_znamenka2 = repr(c)[-1]
zadnja_znamenka3 = repr(d)[-1]
zadnja_znamenka4 = repr(e)[-1]
zadnja_znamenka5 = repr(f)[-1]
l.append(zadnja_znamenka)
l.append(zadnja_znamenka1)
l.append(zadnja_znamenka2)
l.append(zadnja_znamenka3)
l.append(zadnja_znamenka4)
l.append(zadnja_znamenka5)


for i in range(3):          #unošenje 3 jokera
    b = str(input())
    l1.append(list(b))



l.reverse()         #okretanje brojeva jer se gleda od zadnjeg
for i in range(3):
    l1[i].reverse()


for i in range(3):          #prebrojavanje istih brojeva te ispisivanje rezultata
    k = 0
    for j in range(6):
        if l1[i][j] == l[j]:
            k += 1
            if k == 6:
                print ("I. vrsta")
        else:
            if k == 0 or k == 1:
                print ("Nedobitan")
            elif k == 2:
                print ("V. vrsta")
            elif k == 3:
                print ("IV. vrsta")
            elif k == 4:
                print ("III. vrsta")
            elif k == 5:
                print ("II. vrsta")
            break
            



