a = list(input())
b = ['H','Q','9']
for i in range(0,len(a)):
    if a[i] in b:
        print('YES')
        quit()
print('NO')