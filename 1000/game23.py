#https://codeforces.com/problemset/problem/1141/A
n,m=map(int,input().split())
ans=0
if m%n:print(-1);exit()
else:
          x=m//n
          while x%3==0:ans+=1;x//=3
          while x%2==0:ans+=1;x//=2
          if x!=1:print(-1);exit()
print(ans)