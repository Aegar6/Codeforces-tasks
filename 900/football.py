def dang():
    b = 1
    c = 0
    while b != 7:
        if a[c] == a[c+1]:
            b+=1
            c+=1
        else:
            c+=1
            b=1
        if b == 7:
            return('YES')
        if c == len(a)-1:
            break
    return('NO')
a = list(map(int,input()))
print(dang())
    