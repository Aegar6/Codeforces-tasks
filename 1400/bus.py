bus_stops, max_capacity = list(map(int,input().split()))
records = list(map(int,input().split()))
final = []
for start in range(0,max_capacity+1):
    value = start
    exc = True
    #print(f'for {start}')
    for record in records:
        #print(f'{start}+{record}={start+record}')
        start+= record
        if start < 0 or start > max_capacity:
            exc = False
            break
    if exc == False:
        continue
    #print(f'start is {start}')
    #if start >= 0 and start <= max_capacity:
    final.append(value)
    #print(final)
print(len(final))