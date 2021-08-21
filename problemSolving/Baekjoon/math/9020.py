li_primes = [False,False]+ [True]*20000
for i in range(2, int(20000**0.5)+1):
    if li_primes[i]:
        for j in range(2*i,20001,i):
            li_primes[j] = False
T = int(input())
for _ in range(T):
    n = int(input())
    result = dict()
    for p in range(2,2*n):
        if li_primes[p] and n-p>0 and li_primes[n-p]:
            result[max(n-p,p)-min(n-p,p)] = sorted([p,n-p])
    print(' '.join(map(str,result[min(result.keys())])))
