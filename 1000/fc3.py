n = int(input())
hours = []
c = 1
for i in range(0,n):
    x= list(map(int,input().split()))
    hours.append(x)
y= 0
t=0
if hours[0] == hours[-1]:
    c = len(hours)
elif len(hours) > 200:
    for i in range(len(hours)-1):
        if hours[i] == hours[i+1]:
            t+=1
            if t>c:
                c=t
        else:
            if t>c:
                c=t
            t=1   
    if t>c:
        t+=1
        c=t
else:
    while y != len(hours):
        t = hours[y:].count(hours[y])
        if t>c:
            c=t
        y+=t
print(c)