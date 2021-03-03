def gcd(a, b): 
    if (a == 0): 
        return b 
    return gcd(b % a, a) 
def printAllDivisors(arr, N): 
    g = arr[0] 
    divisors = dict() 
    for i in range(1, N): 
        g = gcd(arr[i], g) 
    for i in range(1, g + 1): 
        if i*i > g: 
            break
        if (g % i == 0): 
            divisors[i] = 1
            if (g // i != i): 
                divisors[g // i] = 1
    print(len(divisors))
        
if __name__ == '__main__': 
    n = int(input())
    arr = list(map(int,input().split()))
    printAllDivisors(arr, n) 
  