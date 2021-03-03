row, col = list(map(int,input().split()))
rows = []
for r in range(row):
    rows.append(list(input()))
positions = []
rn = 0
for r in rows:
    pn = 0
    for p in r:
        if p == '*':
            positions.append([rn,pn])
        pn+=1
    rn+=1
bx,by = positions[0]

#unfinished https://codeforces.com/problemset/problem/699/B