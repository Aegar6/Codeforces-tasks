a = list(map(int,input()))
b = 'NO'
a1 = a.count(4)
a2 = a.count(7)
if a2+a1 == 4 or a2+a1 == 7:
    b = 'YES'
print(b)
