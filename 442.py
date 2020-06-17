n = int(input())
l = list(str(n))
a = 0
b = 0
c = 0
for i in range(len(l)-2):
    if int(l[i]) + int(l[i+1]) + int(l[i+2]) == 10:
        a = int(l[i])
        b = int(l[i+1])
        c = int(l[i+2])
print (a,b,c)
    