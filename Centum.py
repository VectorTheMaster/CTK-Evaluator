g = int(input())

k = 101
s = 1

for i in range(24):
    if g<k:
        print (s)
        break
    else:
        k += 100
        s += 1


