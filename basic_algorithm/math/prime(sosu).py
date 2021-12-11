for i in range(2,int(k**0.5)+1):
    if li_primes[i]:
        for j in range(2*i,k+1,i):
            li_primes[j] = False