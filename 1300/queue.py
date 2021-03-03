n_people = int(input())
waiting_times = list(map(int,input().split()))
waiting_times.sort()
time = waiting_times[0]
satissfied = 1
#print(waiting_times)
for i in range(1,len(waiting_times)):
    
    if time <= waiting_times[i]:
        satissfied+=1
        time+=waiting_times[i]
print(satissfied)