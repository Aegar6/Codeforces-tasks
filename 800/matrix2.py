b = []
c = 0
for i in range(0,5):
    a = list(map(int,input().split()))
    b= b+a
bi = b.index(1)
while bi != 12:
    if bi>12:
        b1 = bi-12
        bi = 12 -b1
    if bi<10:
        bi+=5
        c+=1
    else:
        bi+=1
        c+=1
print(c)