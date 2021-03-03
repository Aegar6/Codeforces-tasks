l = 0
u = 0
a = list(input())
for i in range(0,len(a)):
    if a[i].islower():
        l+=1
    else:
        u+=1
a = ''.join(a)
if u>l:
    print(a.upper())      
else:
    print(a.lower())