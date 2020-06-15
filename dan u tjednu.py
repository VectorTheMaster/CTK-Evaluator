a = int(input())
dan = 4
for i in range(a):
    if dan == 6:
        dan = 0
    else:
        dan += 1
if dan>0:
    print (dan-1)
else:
    print (6)