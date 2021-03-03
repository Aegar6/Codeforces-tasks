a = list(map(int,input().split()))
lim = a[0]
bob = a[1]
c=0
while lim<=bob:
    lim*=3
    bob*=2
    c+=1
print(c)