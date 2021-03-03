ale = False
lap = []
n = int(input(''))
for i in range(0,n):
    b= input('')
    b= b.split()
    if b[0] == b[1]:
        continue
    lap = lap + b
    for i in range(0, len(lap)): 
        lap[i] = int(lap[i])
    if len(lap) == 4:
        i = 0
        if (lap[i] < lap[i+1] and lap[i+2] > lap[i+3]) or (lap[i] > lap[i+1] and lap[i+2] < lap[i+3]):
            print('Happy Alex')
            ale = True
            break
        elif lap[i] == lap[i+1] or lap[i+2] == lap[i+3]:
            lap.pop(0)
            lap.pop(0)
            ale = False
        else:
            lap.pop(0)
            lap.pop(0)
            ale = False

if ale == False:
    print('Poor Alex')