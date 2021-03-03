n = input('')
a = list(map(int,input().split()))
m = input('')
b = list(map(int,input().split()))
a.sort()
b.sort()
x=0
for i in a:
  for j in b:
    if -1<=i-j<=1 :
      x += 1
      b.remove(j)
      break
print(x)