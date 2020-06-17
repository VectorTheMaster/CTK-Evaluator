n = int(input())
k = 0
l = []
for i in range(n):
    b = int(input())
    l.append(b)
for j in range(len(l)):
    if l[j] >= j+1:
        k += 1
print (k)
