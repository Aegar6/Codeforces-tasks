a,b,c,n = list(map(int,input().split()))
if a <c or b<c or n<c or n<a or n<b or a+b+c == n:
    print(-1)
    quit()
a-=c
b-=c
if a+b+c == n or a+b> n:
    print(-1)
    quit()
print(n-a-b-c)
