t = input()
l =[]
for i in range(0,int(t)):
    s = input()
    l.append(s)
n=0
for i in range(0,int(t)):
    if len(l[n])>10 :
        a = l[n]

        b = a[0]
        c = a[-1]
        d = len(a[1:-1])
        res = str(b)+ str(d) +str(c)
        print(res)
        
        
        n +=1
        continue
    else:
        print(l[n])
        n +=1
        continue
