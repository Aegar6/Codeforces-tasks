b = 0 #pozycja startowa
k = 0 #kroki
a = int(input())
for i in range(5,0,-1):
    while a-b>=i:
        b+=5
        k+=1
print(k)