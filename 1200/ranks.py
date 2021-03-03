n, k = list(map(int,input().split())) 
ranks = list(map(int,input().split())) 
coin = 0
while sum(ranks) != k*len(ranks):
    temp = []
    for i in range(0,len(ranks)):
        if ranks[i] not in temp and ranks[i] <k:
            temp.append(ranks[i])
            ranks[i]+=1 
    coin+=1
print(coin)
