mounds = int(input())
if mounds == 1:
    print(1)
    quit()
o,h,t,m = 2,mounds//2,mounds,[1]
for i in range(0,mounds//2+1):
    if t > h:
        m.append(t)
        t-=1
    if o <= h:
        m.append(o)
        o+=1
  
print(' '.join(map(str,m)))