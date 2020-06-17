b, n = map(int,input().split())

razlomak = b/n


if razlomak < 0.125:
    print ("0 4")
elif razlomak < 0.374:
    print ("1 4")
elif razlomak < 0.624:
    print ("2 4")
elif razlomak < 0.874:
    print ("3 4")
else:
    print ("4 4")   