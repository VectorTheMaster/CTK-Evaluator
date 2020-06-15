a = 1
zbroj = 0
n = 0
while a != 0:
    a = int(input())
    zbroj += a
    n += 1
print (n)
print (zbroj)
b = zbroj/(n-1)
print (round(b, 2))

