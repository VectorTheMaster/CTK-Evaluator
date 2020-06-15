a, b = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
l = [a1, a2]
l1 = [b1, b2]
l2 = []
l2.extend(l1)
l2.extend(l)
if a>b:
    print (min(l))
elif a == b:
    print (min(l2))
else:
    print (min(l1))
