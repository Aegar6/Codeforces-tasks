from math import pow
h = int(input())
cases= []
k = 1
x = 1
res = 0
for i in range(0,h):
    n = int(input())
    cases.append(n)
for i in range(0,len(cases)):
    while res != cases[i]:
        add = k*x
        res+=add
        x*=2
        if res > cases[i]:
            res = 0
            x = 1
            k+=1
        if cases[i] > 1000:
            k = cases[i]//3
            res = cases[i]
    print(k)
    k=1
    x=1
    res=0
#https://codeforces.com/problemset/problem/1343/A


