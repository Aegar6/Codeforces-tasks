s, l= list(map(int,input().split()))
sig = []
for i in range(s):
    sig.append(list(map(int,input())))
print(sig)
for i in range(0,l):
    out = 0
    for x in range(0,l-1):
        out+=sig[x][i]
    if out > 1:
        print('YES')
        quit()
print('NO') 
    
