tc = int(input())
for i in range(0,tc):
    price_each, n_donuts, price_box = list(map(int,input().split()))
    if price_each >= price_box:
        one = -1
    elif price_box > price_each:
        one = 1
    if price_each*n_donuts > price_box:
        two = n_donuts
    if price_each*n_donuts <= price_box:
        two = -1
    print(one, two)











    #price_each_box = price_each*n_donuts
    #price_box2 = price_box*2
    #price_each_box2 = price_each*(n_donuts*2)
    #if price_each_box2 == price_box2:
    #    print(price_each, -1)
    #elif price_each_box2 > price_box2:
    #    print(-1, n_donuts)
    
    