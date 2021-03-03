f = int(input())
petals = list(map(int,input().split()))
#print(f'suma: {sum(petals)}')
while True:
    if sum(petals)%2 == 1:
        print(sum(petals))
        break
    else:
        try:
            m = min(i for i in petals if i%2)
        except:
            m = min(petals)
        #print(f'removed: {m} ')
        petals.remove(m)
        #print(sum(petals))
        #print(petals)
    if petals == []:
        print(0)
        break