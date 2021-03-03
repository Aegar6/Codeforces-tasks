n,a,b = list(map(int,input().split()))
num = []
ind = []
g = 0
for i in range(0,n):
    c,d =list(map(int,input().split()))
    if c not in ind:
        num.append(d)
        ind.append(c)
for i in num:
    g+=i
if g > b:
    print(b)
else:
    print(g)

https://codeforces.com/problemset/problem/33/A