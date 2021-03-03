s = list(map(int,input().split()))
n = s[0]
m = s[1]
x = 0
while True:
    if n <1 or m<1:
        break
    n-=1
    m-=1
    x+=1
if (x//2)*2 == x:
    print('Malvika')
elif x ==  1:
    print('Akshat')
else:
    print('Akshat')