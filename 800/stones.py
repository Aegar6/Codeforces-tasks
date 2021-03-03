a = int(input())
b = list(input())
c = 0
for i in range(0,a-1):
    if b[i] == b[i+1]:
        c+=1
print(c)
