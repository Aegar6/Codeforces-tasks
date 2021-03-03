want, ava = list(map(int,input().split()))
rodz = list(map(int,input().split()))
rodz.sort()
d = 0
c = 0
for i in range(0,len(rodz)):
    acc = rodz.count(rodz[i])
    if acc == want:
        print(0)
        quit()
for i in range(0,len(rodz)-(want-1)):
    res = rodz[i + want-1] - rodz[i]
    if c == 0:
        d = res
        c+=1
    if res < d:
        d = res
print(d)