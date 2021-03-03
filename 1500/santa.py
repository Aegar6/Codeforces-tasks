s = input('')
t = input('')
li1 = []
li2 = []
out = 0
mis = []
mis2 = []
kis = []
n = 0
for i in range(0,len(s)):
    li1.append(s[n])
    n+=1
n=0
for i in range(0,len(t)):
    li2.append(t[n])
    n+=1
n=0

for i in range(0,len(t)):
    if li2[n] == li1[n]:
        if li1[n] in mis or li2[n] in mis:
            print('-1')
            quit()
        else:
            kis.append(li1[n])
            kis.append(li2[n])
            n+=1
    else:
        if li1[n] in mis or li2[n] in mis: 
            if li1[n] in mis and li2[n] in mis:
                mis21 = (li1[n]+li2[n])
                if mis21 in mis2 or mis21[::-1] in mis2:
                    n+=1
                else:
                    print('-1')
                    quit()
            else:
                    print('-1')
                    quit()
            
        else:
            if li1[n] in kis or li2[n] in kis:
                print('-1')
                quit()
            else:
                mis.append(li1[n])
                mis.append(li2[n])
                mis21 = (li1[n]+li2[n])
                mis2.append(mis21)
                out+=1
                n+=1
n =2
d = len(mis)
d = (d/2) -1
for i in range(0,int(d)):
    mis.insert(n,'\n')
    n+=3
n = 1
d = len(mis)

for i in range(0,int(d)):
    mis.insert(n,' ')
    n+=4

mis = ''.join(mis)
print(out)
print(mis)