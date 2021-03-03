a = list(map(int,input().split()))
cost = a[0]
has = a[1]
wan = a[2]
kosz= 0
for i in range(0,wan+1):
    kosz+= cost*i
kosz-= has
if kosz <= 0:
    kosz = 0
print(kosz)