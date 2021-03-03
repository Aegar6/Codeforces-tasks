list1 = [] 
list2 = []   
a = input('')   
b = input('') 
c = input('') 
ab = a+b
sor= sorted(ab)
ab = "".join(sor)
sor2 = sorted(c)
c = ''.join(sor2)
if ab == c:
    print('YES')
else:
    print('NO')
