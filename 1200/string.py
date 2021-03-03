res = list(input())
res2 = []
res2.append(res[0])
for i in range(1,len(res)):
    if res[i] == res2[-1]:
        pass
    else:
        res2.append(res[i])
if len(res2) !=3:
    print('NO')
    quit()
if 'a' in res and 'b' in res and 'c' in res:
    out = 'YES'
else:
    print('NO')
    quit()
ai,an = res.index('a'), res.count('a')
bi,bn = res.index('b'), res.count('b')
ci,cn = res.index('c'), res.count('c')
maxab = an+bn
if  cn == an or cn == bn:
    out =('YES')
else:
    print('NO')
    quit()
if ai <bi< ci:
    print('YES')
else:
    print('NO')
    quit()
