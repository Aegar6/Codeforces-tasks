a = input('')
a1 = a[0]
if a1.isupper():
    print(a)
    pass
    
else:
    a1 = a1.upper()
    koks =[]
    koks.append(a1)
    koks.append(a[1:len(a)])
    koks = ''.join(koks)
    print(koks)