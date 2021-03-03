n = int(input())
c = list(map(int,input().split()))

all_div = []
res = []
big = max(c)

from math import sqrt
def printDivisors(n) : 
    i = 1
    while i <= sqrt(n): 
          
        if (n % i == 0) : 
              
            # If divisors are equal, print only one 
            if (n / i == i) : 
                all_div.append(i) 
            else : 
                # Otherwise print both 
                all_div.append(i) 
                all_div.append(int(n/i)) 
        i = i + 1

printDivisors(big) 
c.sort(reverse=True)
q = 0
cou = 0

for x in all_div:
    if all(i % x == 0 for i in c):
        q+=1
        

#for x in c:
#    for i in all_div:
#        if x%i != 0:
#            all_div.remove(i)

#print(len(all_div))
   
print(q)
