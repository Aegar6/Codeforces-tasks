a = int(input())
c = a
b = input()
i = 0
while 'RU' in b or 'UR' in b:
    if b[i] == 'R' and b[i+1] == 'U':
        b = b.replace('RU', 'D',1)
        c-=1
    elif b[i] == 'U' and b[i+1] == 'R':
        b = b.replace('UR', 'D',1)
        c-=1
    i+=1
print(len(b))
