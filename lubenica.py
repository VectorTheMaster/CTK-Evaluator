w = int(input())

if w % 6 == 0:
    print ("DA")
elif w == 10:
    print ("DA")
elif w % 2 == 0:
    a = w//2
    if a % 2 == 0:
        print ("DA")
    else:
        print ("NE")

else:
    print ("NE")
