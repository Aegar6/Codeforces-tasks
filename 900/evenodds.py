a = list(map(int,input().split()))
pos = a[1]
len = a[0]
even = []
odd = []
def even_odd(i):
    if (i//2)*2 ==i:
        even.append(i)
    else:
        odd.append(i)

for i in range(1,len+1):
    even_odd(i)
who = odd+even
print(who[pos-1])
#skonczone ale time limit