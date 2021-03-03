# w = max capacity of the bus
# t = 0 = number of people before the first stop
# mint = min number of people at one time
# maxt = max number of people at one time
# minb = min number of people before first stop
# maxb = max number of people before first stop

bus_stops, w = list(map(int,input().split()))
records = list(map(int,input().split()))
final = []
t,mint,maxt =0,0,0
for record in records:
    t+=record
    if t >maxt: maxt=t
    if t <mint: mint=t
    if maxt>w:
        print(0)
        quit()
if mint <0:minb = mint-mint*2
else:minb = 0
if maxt <=0:maxb = w 
else:maxb = w - maxt
if minb > maxb: print(0)
else: print(maxb-minb+1)

