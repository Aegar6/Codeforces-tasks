amount_of_forms = int(input())
lengths_of_worms = list(map(int,input().split()))

for leng in range(0,amount_of_forms-1):
    for leng2 in lengths_of_worms[leng+1:]:
        if int(lengths_of_worms[leng]+leng2) in lengths_of_worms:
            for i in range(amount_of_forms-1):
                if lengths_of_worms[i] == leng2 and i != lengths_of_worms.index(leng2):
                    final = i+1
            try:
                print(lengths_of_worms.index(lengths_of_worms[leng]+leng2)+1,final,leng+1)
            except:
                print(lengths_of_worms.index(lengths_of_worms[leng]+leng2)+1,lengths_of_worms.index(leng2)+1,leng+1)
            quit()
print(-1)
