n,m,a,b = list(map(int,input().split()))
res =[]
c=0
mride=0
while c+m<=n:
    c+=m
    mride+=b
x = n-c
if c !=n:
    if mride+b < mride+ x*a:
        mride+=b
    else:
        mride+=x*a

st = n*a
res.append(mride)
res.append(st)
res.sort()
print(res[0])