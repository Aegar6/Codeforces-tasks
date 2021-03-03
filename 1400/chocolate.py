time = int(input())
secs = list(map(int,input().split()))
i = 1
t = 0
n= 0
c= 0
for i in range(time,0,-1):
    n = 0
    if secs[i-1]+secs[i-2] > 200:
        n+=2
        i-=1
        while secs[i-1]+secs[i-2] > 200:
            n+=1
            i-=1
    elif secs[i-1] > 100:
        n+=1
    if n>c:
        c=n
print(c)