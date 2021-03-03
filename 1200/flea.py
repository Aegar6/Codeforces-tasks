quant = int(input())
pos = 1
n = list(range(1,quant+1))
for i in range(0,quant+1):
    pos+= i
    while pos> quant:
        pos-=quant
    if pos in n:
        n.remove(pos)
if len(n) == 0:
    print('YES')
else:
    print('NO')