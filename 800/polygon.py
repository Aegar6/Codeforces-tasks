t = int(input())
num = []
for i in range(0,t):
    a = int(input())
    num.append(a)
for i in range(0,t):
    if num[i]%4 == 0:
        print('YES')
    else:
        print('NO')