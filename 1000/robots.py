n,k = list(map(int,input().split()))
ids= list(map(int,input().split())) 
x=0
i=1
while x+i<k:
   x+=i
   i+=1
res=k-x
print(ids[res-1])
